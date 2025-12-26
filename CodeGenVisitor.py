from llvmlite import ir

from RelationalLangParser import RelationalLangParser
from RelationalLangVisitor import RelationalLangVisitor


class CodeGenVisitor(RelationalLangVisitor):
    def __init__(self):
        self.module = ir.Module(name="relational_module")
        self.builder = None
        self.func = None

        # Таблица символов для LLVM (хранит указатели на память)
        # { 'var_name': ir.AllocaInstr }
        self.symbol_table = {}

        self.void_type = ir.VoidType()
        self.int_type = ir.IntType(32)
        self.float_type = ir.DoubleType()
        self.string_type = ir.IntType(8).as_pointer()
        self.table_type = ir.IntType(8).as_pointer()
        self.table_type = ir.IntType(8).as_pointer()

        self._declare_external_functions()

    def _declare_external_functions(self):
        # Печать
        self.print_str = ir.Function(self.module, ir.FunctionType(self.void_type, [self.string_type]),
                                     name="_print_str")
        self.print_int = ir.Function(self.module, ir.FunctionType(self.void_type, [self.int_type]), name="_print_int")
        self.print_float = ir.Function(self.module, ir.FunctionType(self.void_type, [self.float_type]),
                                       name="_print_float")

        # БД
        self.create_table = ir.Function(self.module, ir.FunctionType(self.table_type, [self.string_type]),
                                        name="_create_table")
        self.add_column = ir.Function(self.module, ir.FunctionType(self.void_type, [self.table_type, self.string_type,
                                                                                    self.string_type]),
                                      name="_add_column")

        # Builder для строк
        self.row_init = ir.Function(self.module, ir.FunctionType(self.void_type, []), name="_row_init")
        self.row_add_int = ir.Function(self.module, ir.FunctionType(self.void_type, [self.int_type]),
                                       name="_row_add_int")
        self.row_add_float = ir.Function(self.module, ir.FunctionType(self.void_type, [self.float_type]),
                                         name="_row_add_float")
        self.row_add_string = ir.Function(self.module, ir.FunctionType(self.void_type, [self.string_type]),
                                          name="_row_add_string")
        self.insert_row_commit = ir.Function(self.module, ir.FunctionType(self.void_type, [self.table_type]),
                                             name="_insert_row_commit")

        self.print_table_full = ir.Function(self.module, ir.FunctionType(self.void_type, [self.table_type]),
                                            name="_print_table_full")

    def save_ir(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.module))

    def visitProgram(self, ctx):
        func_type = ir.FunctionType(self.int_type, [])
        self.func = ir.Function(self.module, func_type, name="main")
        block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        for child in ctx.children:
            if isinstance(child, RelationalLangParser.StatementContext):
                self.visit(child)

        self.builder.ret(ir.Constant(self.int_type, 0))


    def visitAssignStmt(self, ctx):
        var_name = ctx.pathExpr().getText()
        val = self.visit(ctx.expr())

        if val is None:
            return

        if var_name not in self.symbol_table:
            with self.builder.goto_entry_block():
                ptr = self.builder.alloca(val.type, name=var_name)
            self.symbol_table[var_name] = ptr

        ptr = self.symbol_table[var_name]
        if val.type != ptr.type.pointee:
            if val.type == self.int_type and ptr.type.pointee == self.float_type:
                val = self.builder.sitofp(val, self.float_type)
            elif val.type == self.float_type and ptr.type.pointee == self.int_type:
                val = self.builder.fptosi(val, self.int_type)

        self.builder.store(val, ptr)

    def visitIfStmt(self, ctx):
        cond_val = self.visit(ctx.expr())

        if cond_val.type == self.int_type:
            cond_bool = self.builder.icmp_signed('!=', cond_val, ir.Constant(self.int_type, 0))
        elif cond_val.type == self.float_type:
            cond_bool = self.builder.fcmp_ordered('!=', cond_val, ir.Constant(self.float_type, 0.0))
        else:
            cond_bool = cond_val

        then_block = self.func.append_basic_block(name="then")
        else_block = self.func.append_basic_block(name="else")
        merge_block = self.func.append_basic_block(name="merge")

        has_else = len(ctx.statement()) > 1

        self.builder.cbranch(cond_bool, then_block, else_block)

        self.builder.position_at_start(then_block)

        all_stmts = ctx.statement()

        stmts_then = []
        stmts_else = []
        is_else = False
        for child in ctx.children:
            if child.getText() == 'else':
                is_else = True
                continue
            if isinstance(child, RelationalLangParser.StatementContext):
                if is_else:
                    stmts_else.append(child)
                else:
                    stmts_then.append(child)

        for stmt in stmts_then:
            self.visit(stmt)

        if not self.builder.block.is_terminated:
            self.builder.branch(merge_block)

        self.builder.position_at_start(else_block)
        for stmt in stmts_else:
            self.visit(stmt)

        if not self.builder.block.is_terminated:
            self.builder.branch(merge_block)

        self.builder.position_at_start(merge_block)

    def visitLiteralExpr(self, ctx):
        if ctx.literal().INT():
            return ir.Constant(self.int_type, int(ctx.getText()))
        if ctx.literal().FLOAT():
            return ir.Constant(self.float_type, float(ctx.getText()))
        if ctx.literal().STRING():
            text = ctx.getText().strip('"') + '\0'
            c_str_val = ir.Constant(ir.ArrayType(ir.IntType(8), len(text)), bytearray(text.encode("utf8")))
            global_var = ir.GlobalVariable(self.module, c_str_val.type, name=self.module.get_unique_name("str"))
            global_var.linkage = 'internal'
            global_var.global_constant = True
            global_var.initializer = c_str_val
            return self.builder.bitcast(global_var, self.string_type)

    def visitIdExpr(self, ctx):
        var_name = ctx.pathExpr().getText()
        ptr = self.symbol_table.get(var_name)
        if ptr:
            return self.builder.load(ptr, name=var_name)
        return ir.Constant(self.int_type, 0)

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.type != right.type:
            if left.type == self.int_type: left = self.builder.sitofp(left, self.float_type)
            if right.type == self.int_type: right = self.builder.sitofp(right, self.float_type)

        if ctx.PLUS():
            if left.type == self.int_type:
                return self.builder.add(left, right, name="add")
            else:
                return self.builder.fadd(left, right, name="fadd")
        elif ctx.MINUS():
            if left.type == self.int_type:
                return self.builder.sub(left, right, name="sub")
            else:
                return self.builder.fsub(left, right, name="fsub")

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.type != right.type:
            if left.type == self.int_type: left = self.builder.sitofp(left, self.float_type)
            if right.type == self.int_type: right = self.builder.sitofp(right, self.float_type)

        if ctx.STAR():
            if left.type == self.int_type:
                return self.builder.mul(left, right, name="mul")
            else:
                return self.builder.fmul(left, right, name="fmul")
        elif ctx.SLASH():  # Деление
            if left.type == self.int_type:
                return self.builder.sdiv(left, right, name="div")
            else:
                return self.builder.fdiv(left, right, name="fdiv")

    def visitCompareExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left.type != right.type:
            if left.type == self.int_type: left = self.builder.sitofp(left, self.float_type)
            if right.type == self.int_type: right = self.builder.sitofp(right, self.float_type)

        op = ''
        if ctx.GT():
            op = '>'
        elif ctx.LT():
            op = '<'
        elif ctx.GE():
            op = '>='
        elif ctx.LE():
            op = '<='
        elif ctx.EQ():
            op = '=='
        elif ctx.NEQ():
            op = '!='

        if left.type == self.int_type:
            return self.builder.icmp_signed(op, left, right, name="icmp")
        else:
            return self.builder.fcmp_ordered(op, left, right, name="fcmp")

    def visitNewExpr(self, ctx):
        return ir.Constant(self.table_type, None)

    def visitCastExpr(self, ctx):
        val = self.visit(ctx.expr())
        target_type = ctx.typeDecl().getText()

        if target_type == 'float' and val.type == self.int_type:
            return self.builder.sitofp(val, self.float_type, name="cast_to_float")
        if target_type == 'int' and val.type == self.float_type:
            return self.builder.fptosi(val, self.int_type, name="cast_to_int")

        return val

    def visitMethodCallExpr(self, ctx):
        return ir.Constant(self.int_type, 0)

    def visitMethodCallStmt(self, ctx):
        pass

    def visitFuncCallExpr(self, ctx):
        func_name = ctx.ID().getText()

        if func_name == "insert_row":
            table_arg = self.visit(ctx.exprList().expr(0))
            row_literal = ctx.exprList().expr(1)  # { ... }

            self.builder.call(self.row_init, [])

            if row_literal.exprList():
                for val_ctx in row_literal.exprList().expr():
                    val_ir = self.visit(val_ctx)

                    if val_ir.type == self.int_type:
                        self.builder.call(self.row_add_int, [val_ir])
                    elif val_ir.type == self.float_type:
                        self.builder.call(self.row_add_float, [val_ir])
                    elif val_ir.type == self.string_type:
                        self.builder.call(self.row_add_string, [val_ir])

            return self.builder.call(self.insert_row_commit, [table_arg])

        args = []
        if ctx.exprList():
            for e in ctx.exprList().expr():
                args.append(self.visit(e))

        if func_name == "write":
            if not args:
                return ir.Constant(self.int_type, 0)

            arg = args[0]
            if arg.type == self.string_type:
                return self.builder.call(self.print_str, [arg])
            elif arg.type == self.int_type:
                return self.builder.call(self.print_int, [arg])
            elif arg.type == self.float_type:
                return self.builder.call(self.print_float, [arg])

        elif func_name == "create_table":
            return self.builder.call(self.create_table, args)
        elif func_name == "add_column":
            return self.builder.call(self.add_column, args)
        elif func_name == "print_table":
            return self.builder.call(self.print_table_full, args)

        return ir.Constant(self.int_type, 0)

    def visitFuncCallStmt(self, ctx):
        self.visitFuncCallExpr(ctx)