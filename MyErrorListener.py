from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Ошибка синтаксиса [Строка {line}:{column}]: {msg}"
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def print_errors(self):
        for err in self.errors:
            print(err)