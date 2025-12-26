from RelationalLangVisitor import RelationalLangVisitor
from RelationalLangParser import RelationalLangParser
from SymbolTable import *


class SemanticVisitor(RelationalLangVisitor):
    def __init__(self):
        self.errors = []
        self.global_scope = ScopedSymbolTable("GLOBAL")
        self.current_scope = self.global_scope
        self.current_struct = None

        self.global_scope.define(FunctionSymbol("create_table", "table", ["string"]))
        self.global_scope.define(FunctionSymbol("add_column", "void", ["table", "string", "string"]))
        self.global_scope.define(FunctionSymbol("insert_row", "void", ["table", "row"]))
        self.global_scope.define(FunctionSymbol("write", "void", []))
        self.global_scope.define(FunctionSymbol("filter", "table", ["table", "string"]))
        self.global_scope.define(FunctionSymbol("print_table", "void", ["table"]))

    def add_error(self, ctx, msg):
        line = ctx.start.line
        self.errors.append(f"Семантическая ошибка [Строка {line}]: {msg}")

    def visitProgram(self, ctx):
        for child in ctx.children:
            if isinstance(child, RelationalLangParser.StructDeclContext):
                self.register_struct(child)

        for child in ctx.children:
            if isinstance(child, RelationalLangParser.SubroutineDeclContext):
                self.register_subroutine(child)

        return self.visitChildren(ctx)

    def register_struct(self, ctx):
        name = ctx.ID(0).getText()
        parent = ctx.ID(1).getText() if ctx.EXTENDS() else None

        if self.global_scope.resolve(name):
            self.add_error(ctx, f"Структура '{name}' уже объявлена.")
            return

        struct_sym = StructSymbol(name, parent)
        for member in ctx.memberDecl():
            m_name = member.ID().getText()
            m_type = member.typeDecl().getText()
            struct_sym.members[m_name] = m_type

        self.global_scope.define(struct_sym)

    def register_subroutine(self, ctx):
        name = ctx.ID().getText()
        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                params.append(p.typeDecl().getText())

        if self.global_scope.resolve(name):
            self.add_error(ctx, f"Подпрограмма '{name}' уже объявлена.")
        else:
            self.global_scope.define(FunctionSymbol(name, "void", params))

    def visitStructDecl(self, ctx):
        struct_name = ctx.ID(0).getText()
        self.current_struct = self.global_scope.resolve(struct_name)
        for method in ctx.methodDecl():
            self.visit(method)
        self.current_struct = None

    def visitSubroutineDecl(self, ctx):
        prev_scope = self.current_scope
        self.current_scope = ScopedSymbolTable(ctx.ID().getText(), prev_scope)

        if ctx.paramList():
            for p in ctx.paramList().param():
                p_name = p.ID().getText()
                p_type = p.typeDecl().getText()
                self.current_scope.define(VariableSymbol(p_name, p_type))

        for stmt in ctx.statement():
            self.visit(stmt)
        self.current_scope = prev_scope

    def visitMethodDecl(self, ctx):
        prev_scope = self.current_scope
        self.current_scope = ScopedSymbolTable(ctx.ID().getText(), prev_scope)

        self.current_scope.define(VariableSymbol("self", self.current_struct.name))

        if ctx.paramList():
            for p in ctx.paramList().param():
                p_name = p.ID().getText()
                p_type = p.typeDecl().getText()
                self.current_scope.define(VariableSymbol(p_name, p_type))

        for stmt in ctx.statement():
            self.visit(stmt)
        self.current_scope = prev_scope

    def visitForStmt(self, ctx):
        prev_scope = self.current_scope
        self.current_scope = ScopedSymbolTable("FOR", prev_scope)

        var_type = ctx.typeDecl().getText()
        var_name = ctx.ID().getText()
        if var_type not in ["table", "row", "column"]:
            if not self.global_scope.resolve(var_type):
                self.add_error(ctx, f"Структура '{var_type}' не определена.")
                return

        self.current_scope.define(VariableSymbol(var_name, var_type))

        for stmt in ctx.statement():
            self.visit(stmt)
        self.current_scope = prev_scope

    def visitAssignStmt(self, ctx):
        right_type = self.visit(ctx.expr())
        path = ctx.pathExpr()
        ids = [node.getText() for node in path.ID()]
        var_name = ids[0]

        var_sym = self.current_scope.resolve(var_name)

        if not var_sym:
            if len(ids) == 1:
                self.current_scope.define(VariableSymbol(var_name, right_type))
                return
            else:
                self.add_error(ctx, f"Переменная '{var_name}' не объявлена.")
                return

        current_type_name = var_sym.type_name
        for field in ids[1:]:
            if current_type_name == "row":
                return

            struct_sym = self.global_scope.resolve(current_type_name)
            if not isinstance(struct_sym, StructSymbol):
                self.add_error(ctx, f"Тип '{current_type_name}' не является структурой.")
                return

            member_type = struct_sym.resolve_member(field, self.global_scope)
            if not member_type:
                self.add_error(ctx, f"У структуры '{struct_sym.name}' нет поля '{field}'.")
                return
            current_type_name = member_type

        if current_type_name != right_type and right_type != "any":
            if current_type_name == "float" and right_type == "int":
                pass
            elif current_type_name == "table" and right_type == "table":
                pass  # Разрешаем table = table
            else:
                self.add_error(ctx, f"Несовместимые типы: ожидался '{current_type_name}', получен '{right_type}'.")

    def visitFuncCallExpr(self, ctx):
        func_name = ctx.ID().getText()
        sym = self.global_scope.resolve(func_name)

        if not sym:
            self.add_error(ctx, f"Функция '{func_name}' не найдена.")
            return "any"

        if not isinstance(sym, FunctionSymbol):
            self.add_error(ctx, f"'{func_name}' не является функцией.")
            return "any"

        if func_name == "write":
            return "void"

        expected_count = len(sym.params)
        given_count = 0
        if ctx.exprList():
            given_count = len(ctx.exprList().expr())

        if expected_count != given_count:
            self.add_error(ctx, f"Функция '{func_name}' ожидает {expected_count} аргументов, получено {given_count}.")
            return "any"

        return sym.type_name

    def visitMethodCallExpr(self, ctx):
        obj_type = self.visit(ctx.expr())
        method_name = ctx.ID().getText()

        if obj_type == "any": return "any"

        struct_sym = self.global_scope.resolve(obj_type)
        if not isinstance(struct_sym, StructSymbol):
            self.add_error(ctx, f"Тип '{obj_type}' не имеет методов (не структура).")
            return "any"

        return "void"

    def visitFuncCallStmt(self, ctx):
        self.visitFuncCallExpr(ctx)

    def visitMethodCallStmt(self, ctx):
        self.visitMethodCallExpr(ctx)

    def visitLiteralExpr(self, ctx):
        if ctx.literal().INT(): return "int"
        if ctx.literal().FLOAT(): return "float"
        if ctx.literal().STRING(): return "string"
        return "any"

    def visitIdExpr(self, ctx):
        ids = [node.getText() for node in ctx.pathExpr().ID()]
        var_name = ids[0]

        sym = self.current_scope.resolve(var_name)
        if not sym:
            self.add_error(ctx, f"Переменная '{var_name}' не найдена.")
            return "any"

        current_type = sym.type_name

        for field in ids[1:]:
            if current_type == "row":
                return "any"

            struct_sym = self.global_scope.resolve(current_type)
            if isinstance(struct_sym, StructSymbol):
                member_type = struct_sym.resolve_member(field, self.global_scope)
                if member_type:
                    current_type = member_type
                else:
                    self.add_error(ctx, f"Поле '{field}' не найдено.")
                    return "any"
            else:
                self.add_error(ctx, f"'{current_type}' не является структурой.")
                return "any"

        return current_type

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left == "any" or right == "any":
            return "any"

        if ctx.MINUS():
            if left not in ['int', 'float'] or right not in ['int', 'float']:
                self.add_error(ctx, f"Нельзя вычитать типы '{left}' и '{right}'.")
                return "any"
            if left == 'float' or right == 'float': return 'float'
            return 'int'

        if ctx.PLUS():
            if left == 'string' and right == 'string':
                return 'string'

            if left in ['int', 'float'] and right in ['int', 'float']:
                if left == 'float' or right == 'float': return 'float'
                return 'int'

            self.add_error(ctx, f"Нельзя складывать типы '{left}' и '{right}'.")
            return "any"

        return "any"

    def visitNewExpr(self, ctx):
        struct_name = ctx.ID().getText()
        if not self.global_scope.resolve(struct_name):
            self.add_error(ctx, f"Структура '{struct_name}' не определена.")
        return struct_name

    def visitCastExpr(self, ctx):
        return ctx.typeDecl().getText()

    def visitChildren(self, node):
        result = "any"
        for c in node.getChildren():
            child_result = c.accept(self)
            if child_result: result = child_result
        return result