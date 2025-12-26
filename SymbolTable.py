class Symbol:
    def __init__(self, name, type_name):
        self.name = name
        self.type_name = type_name

class VariableSymbol(Symbol):
    pass

class FunctionSymbol(Symbol):
    def __init__(self, name, type_name, params):
        super().__init__(name, type_name)
        self.params = params

class StructSymbol(Symbol):
    def __init__(self, name, parent_name=None):
        super().__init__(name, name)
        self.parent_name = parent_name
        self.members = {}
        self.methods = {}

    def resolve_member(self, member_name, global_scope):
        if member_name in self.members:
            return self.members[member_name]
        if self.parent_name:
            parent = global_scope.resolve(self.parent_name)
            if parent and isinstance(parent, StructSymbol):
                return parent.resolve_member(member_name, global_scope)
        return None

class ScopedSymbolTable:
    def __init__(self, scope_name, parent_scope=None):
        self.scope_name = scope_name
        self.parent_scope = parent_scope
        self.symbols = {}

    def define(self, symbol):
        self.symbols[symbol.name] = symbol

    def resolve(self, name):
        if name in self.symbols:
            return self.symbols[name]
        if self.parent_scope:
            return self.parent_scope.resolve(name)
        return None