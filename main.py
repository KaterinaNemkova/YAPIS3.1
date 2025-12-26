import subprocess
import os
import sys
from antlr4 import *

from CodeGenVisitor import CodeGenVisitor
from RelationalLangLexer import RelationalLangLexer
from RelationalLangParser import RelationalLangParser
from MyErrorListener import MyErrorListener
from SemanticVisitor import SemanticVisitor


def main(input_file):
    print(f"--- Анализ файла: {input_file} ---")

    # 1. Чтение файла
    try:
        input_stream = FileStream(input_file, encoding='utf-8')
    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")
        return

    # 2. Лексический анализ (разбиение на токены)
    lexer = RelationalLangLexer(input_stream)
    lexer_error_listener = MyErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)
    stream = CommonTokenStream(lexer)

    # 2. Синтаксический анализ
    parser = RelationalLangParser(stream)
    parser_error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)
    tree = parser.program()

    if lexer_error_listener.has_errors() or parser_error_listener.has_errors():
        print("НАЙДЕНЫ СИНТАКСИЧЕСКИЕ ОШИБКИ:")
        lexer_error_listener.print_errors()
        parser_error_listener.print_errors()
        print(">>> Компиляция ПРЕРВАНА (Синтаксис).")
        print("-" * 30 + "\n")
        return
    print("Синтаксис: OK")

    semantic_visitor = SemanticVisitor()
    semantic_visitor.visit(tree)

    if semantic_visitor.errors:
        print("НАЙДЕНЫ СЕМАНТИЧЕСКИЕ ОШИБКИ:")
        for err in semantic_visitor.errors:
            print(err)
        print(">>> Компиляция ПРЕРВАНА (Семантика).")
        print("-" * 30 + "\n")
        return

    print("Семантика: OK. Генерация кода...")

    codegen = CodeGenVisitor()
    codegen.visit(tree)

    output_file = input_file.replace(".txt", ".ll")
    codegen.save_ir(output_file)
    print(f"Сгенерирован файл: {output_file}")

    exe_file = input_file.replace(".txt", ".exe")

    clang_path = r"C:\msys64\clang64\bin\clang.exe"
    if not os.path.exists(clang_path):
        clang_path = "clang"

    try:
        cmd = [clang_path, output_file, "runtime.c", "-o", exe_file]
        print(f"Запуск компиляции: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        print(f"УСПЕШНО СОЗДАН: {exe_file}")

        print("\n--- ЗАПУСК ПРОГРАММЫ ---")
        subprocess.run([exe_file])

    except FileNotFoundError:
        print("ОШИБКА: Clang не найден.")
    except subprocess.CalledProcessError:
        print("ОШИБКА: Не удалось скомпилировать EXE.")

    print("-" * 30 + "\n")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            main(filename)
    else:

        test_dirs = [
            os.path.join("tests", "valid"),
            os.path.join("tests", "errors"),
            os.path.join("tests", "semantic_errors"),
            os.path.join("tests", "mixed"),
            os.path.join("tests", "code")
        ]

        for folder in test_dirs:
            if os.path.exists(folder):
                print(f"\n{'=' * 20} ЗАПУСК ТЕСТОВ ИЗ ПАПКИ: {folder} {'=' * 20}")

                files = os.listdir(folder)

                files.sort()

                for f in files:
                    if f.endswith(".txt"):
                        full_path = os.path.join(folder, f)
                        main(full_path)
            else:
                print(f"\n[ВНИМАНИЕ] Папка не найдена: {folder}")