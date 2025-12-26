# Generated from RelationalLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RelationalLangParser import RelationalLangParser
else:
    from RelationalLangParser import RelationalLangParser

# This class defines a complete generic visitor for a parse tree produced by RelationalLangParser.

class RelationalLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RelationalLangParser#program.
    def visitProgram(self, ctx:RelationalLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#structDecl.
    def visitStructDecl(self, ctx:RelationalLangParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#memberDecl.
    def visitMemberDecl(self, ctx:RelationalLangParser.MemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#methodDecl.
    def visitMethodDecl(self, ctx:RelationalLangParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#subroutineDecl.
    def visitSubroutineDecl(self, ctx:RelationalLangParser.SubroutineDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#paramList.
    def visitParamList(self, ctx:RelationalLangParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#param.
    def visitParam(self, ctx:RelationalLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#statement.
    def visitStatement(self, ctx:RelationalLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#assignStmt.
    def visitAssignStmt(self, ctx:RelationalLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#pathExpr.
    def visitPathExpr(self, ctx:RelationalLangParser.PathExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#funcCallStmt.
    def visitFuncCallStmt(self, ctx:RelationalLangParser.FuncCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#methodCallStmt.
    def visitMethodCallStmt(self, ctx:RelationalLangParser.MethodCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#ifStmt.
    def visitIfStmt(self, ctx:RelationalLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#forStmt.
    def visitForStmt(self, ctx:RelationalLangParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#returnStmt.
    def visitReturnStmt(self, ctx:RelationalLangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#RowLiteral.
    def visitRowLiteral(self, ctx:RelationalLangParser.RowLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:RelationalLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#IdExpr.
    def visitIdExpr(self, ctx:RelationalLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#CompareExpr.
    def visitCompareExpr(self, ctx:RelationalLangParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#CastExpr.
    def visitCastExpr(self, ctx:RelationalLangParser.CastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#NewExpr.
    def visitNewExpr(self, ctx:RelationalLangParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:RelationalLangParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#ParenExpr.
    def visitParenExpr(self, ctx:RelationalLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:RelationalLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:RelationalLangParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#MethodCallExpr.
    def visitMethodCallExpr(self, ctx:RelationalLangParser.MethodCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#exprList.
    def visitExprList(self, ctx:RelationalLangParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#typeDecl.
    def visitTypeDecl(self, ctx:RelationalLangParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#literal.
    def visitLiteral(self, ctx:RelationalLangParser.LiteralContext):
        return self.visitChildren(ctx)



del RelationalLangParser