# Generated from RelationalLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,285,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,54,8,1,
        1,1,1,1,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,1,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,79,8,3,1,3,1,3,1,3,1,3,5,
        3,85,8,3,10,3,12,3,88,9,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,98,
        8,4,1,4,1,4,1,4,1,4,5,4,104,8,4,10,4,12,4,107,9,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,5,5,116,8,5,10,5,12,5,119,9,5,1,6,3,6,122,8,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,145,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,154,
        8,9,10,9,12,9,157,9,9,1,10,1,10,1,10,3,10,162,8,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,3,11,171,8,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,5,12,181,8,12,10,12,12,12,184,9,12,1,12,1,12,1,12,1,12,
        1,12,5,12,191,8,12,10,12,12,12,194,9,12,3,12,196,8,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,210,8,13,
        10,13,12,13,213,9,13,1,13,1,13,1,13,1,14,1,14,3,14,220,8,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,232,8,15,1,15,
        1,15,1,15,1,15,3,15,238,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,3,15,249,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,3,15,265,8,15,1,15,5,15,268,8,15,10,
        15,12,15,271,9,15,1,16,1,16,1,16,5,16,276,8,16,10,16,12,16,279,9,
        16,1,17,1,17,1,18,1,18,1,18,0,1,30,19,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,0,5,1,0,38,39,1,0,36,37,1,0,40,45,1,0,14,
        21,1,0,22,24,311,0,44,1,0,0,0,2,49,1,0,0,0,4,69,1,0,0,0,6,74,1,0,
        0,0,8,93,1,0,0,0,10,112,1,0,0,0,12,121,1,0,0,0,14,144,1,0,0,0,16,
        146,1,0,0,0,18,150,1,0,0,0,20,158,1,0,0,0,22,165,1,0,0,0,24,174,
        1,0,0,0,26,200,1,0,0,0,28,217,1,0,0,0,30,248,1,0,0,0,32,272,1,0,
        0,0,34,280,1,0,0,0,36,282,1,0,0,0,38,43,3,2,1,0,39,43,3,8,4,0,40,
        43,3,14,7,0,41,43,5,26,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,
        0,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,
        1,0,0,0,46,44,1,0,0,0,47,48,5,0,0,1,48,1,1,0,0,0,49,50,5,1,0,0,50,
        53,5,21,0,0,51,52,5,2,0,0,52,54,5,21,0,0,53,51,1,0,0,0,53,54,1,0,
        0,0,54,55,1,0,0,0,55,56,5,3,0,0,56,62,5,26,0,0,57,61,3,4,2,0,58,
        61,3,6,3,0,59,61,5,26,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,
        0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,
        1,0,0,0,65,66,5,5,0,0,66,67,5,1,0,0,67,68,5,26,0,0,68,3,1,0,0,0,
        69,70,5,21,0,0,70,71,5,34,0,0,71,72,3,34,17,0,72,73,5,26,0,0,73,
        5,1,0,0,0,74,75,5,4,0,0,75,76,5,21,0,0,76,78,5,28,0,0,77,79,3,10,
        5,0,78,77,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,81,5,29,0,0,81,
        86,5,26,0,0,82,85,3,14,7,0,83,85,5,26,0,0,84,82,1,0,0,0,84,83,1,
        0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,
        86,1,0,0,0,89,90,5,5,0,0,90,91,5,4,0,0,91,92,5,26,0,0,92,7,1,0,0,
        0,93,94,5,6,0,0,94,95,5,21,0,0,95,97,5,28,0,0,96,98,3,10,5,0,97,
        96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,29,0,0,100,105,5,
        26,0,0,101,104,3,14,7,0,102,104,5,26,0,0,103,101,1,0,0,0,103,102,
        1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,
        1,0,0,0,107,105,1,0,0,0,108,109,5,5,0,0,109,110,5,6,0,0,110,111,
        5,26,0,0,111,9,1,0,0,0,112,117,3,12,6,0,113,114,5,32,0,0,114,116,
        3,12,6,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,
        1,0,0,0,118,11,1,0,0,0,119,117,1,0,0,0,120,122,5,7,0,0,121,120,1,
        0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,3,34,17,0,124,125,
        5,21,0,0,125,13,1,0,0,0,126,127,3,16,8,0,127,128,5,26,0,0,128,145,
        1,0,0,0,129,130,3,20,10,0,130,131,5,26,0,0,131,145,1,0,0,0,132,133,
        3,22,11,0,133,134,5,26,0,0,134,145,1,0,0,0,135,136,3,24,12,0,136,
        137,5,26,0,0,137,145,1,0,0,0,138,139,3,26,13,0,139,140,5,26,0,0,
        140,145,1,0,0,0,141,142,3,28,14,0,142,143,5,26,0,0,143,145,1,0,0,
        0,144,126,1,0,0,0,144,129,1,0,0,0,144,132,1,0,0,0,144,135,1,0,0,
        0,144,138,1,0,0,0,144,141,1,0,0,0,145,15,1,0,0,0,146,147,3,18,9,
        0,147,148,5,35,0,0,148,149,3,30,15,0,149,17,1,0,0,0,150,155,5,21,
        0,0,151,152,5,33,0,0,152,154,5,21,0,0,153,151,1,0,0,0,154,157,1,
        0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,19,1,0,0,0,157,155,1,0,
        0,0,158,159,5,21,0,0,159,161,5,28,0,0,160,162,3,32,16,0,161,160,
        1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,164,5,29,0,0,164,21,
        1,0,0,0,165,166,3,30,15,0,166,167,5,33,0,0,167,168,5,21,0,0,168,
        170,5,28,0,0,169,171,3,32,16,0,170,169,1,0,0,0,170,171,1,0,0,0,171,
        172,1,0,0,0,172,173,5,29,0,0,173,23,1,0,0,0,174,175,5,8,0,0,175,
        176,3,30,15,0,176,177,5,34,0,0,177,182,5,26,0,0,178,181,3,14,7,0,
        179,181,5,26,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,184,1,0,0,0,
        182,180,1,0,0,0,182,183,1,0,0,0,183,195,1,0,0,0,184,182,1,0,0,0,
        185,186,5,9,0,0,186,187,5,34,0,0,187,192,5,26,0,0,188,191,3,14,7,
        0,189,191,5,26,0,0,190,188,1,0,0,0,190,189,1,0,0,0,191,194,1,0,0,
        0,192,190,1,0,0,0,192,193,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,
        0,195,185,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,198,5,5,0,
        0,198,199,5,8,0,0,199,25,1,0,0,0,200,201,5,10,0,0,201,202,3,34,17,
        0,202,203,5,21,0,0,203,204,5,11,0,0,204,205,3,30,15,0,205,206,5,
        34,0,0,206,211,5,26,0,0,207,210,3,14,7,0,208,210,5,26,0,0,209,207,
        1,0,0,0,209,208,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,214,1,0,0,0,213,211,1,0,0,0,214,215,5,5,0,0,215,216,
        5,10,0,0,216,27,1,0,0,0,217,219,5,12,0,0,218,220,3,30,15,0,219,218,
        1,0,0,0,219,220,1,0,0,0,220,29,1,0,0,0,221,222,6,15,-1,0,222,223,
        5,28,0,0,223,224,3,34,17,0,224,225,5,29,0,0,225,226,3,30,15,11,226,
        249,1,0,0,0,227,249,3,18,9,0,228,249,3,36,18,0,229,231,5,30,0,0,
        230,232,3,32,16,0,231,230,1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,
        0,233,249,5,31,0,0,234,235,5,21,0,0,235,237,5,28,0,0,236,238,3,32,
        16,0,237,236,1,0,0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,249,5,29,
        0,0,240,241,5,13,0,0,241,242,5,21,0,0,242,243,5,28,0,0,243,249,5,
        29,0,0,244,245,5,28,0,0,245,246,3,30,15,0,246,247,5,29,0,0,247,249,
        1,0,0,0,248,221,1,0,0,0,248,227,1,0,0,0,248,228,1,0,0,0,248,229,
        1,0,0,0,248,234,1,0,0,0,248,240,1,0,0,0,248,244,1,0,0,0,249,269,
        1,0,0,0,250,251,10,4,0,0,251,252,7,0,0,0,252,268,3,30,15,5,253,254,
        10,3,0,0,254,255,7,1,0,0,255,268,3,30,15,4,256,257,10,2,0,0,257,
        258,7,2,0,0,258,268,3,30,15,3,259,260,10,6,0,0,260,261,5,33,0,0,
        261,262,5,21,0,0,262,264,5,28,0,0,263,265,3,32,16,0,264,263,1,0,
        0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,268,5,29,0,0,267,250,1,0,
        0,0,267,253,1,0,0,0,267,256,1,0,0,0,267,259,1,0,0,0,268,271,1,0,
        0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,31,1,0,0,0,271,269,1,0,0,
        0,272,277,3,30,15,0,273,274,5,32,0,0,274,276,3,30,15,0,275,273,1,
        0,0,0,276,279,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,33,1,0,
        0,0,279,277,1,0,0,0,280,281,7,3,0,0,281,35,1,0,0,0,282,283,7,4,0,
        0,283,37,1,0,0,0,32,42,44,53,60,62,78,84,86,97,103,105,117,121,144,
        155,161,170,180,182,190,192,195,209,211,219,231,237,248,264,267,
        269,277
    ]

class RelationalLangParser ( Parser ):

    grammarFileName = "RelationalLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'extends'", "'is'", "'method'", 
                     "'end'", "'sub'", "'ref'", "'if'", "'else'", "'for'", 
                     "'in'", "'return'", "'new'", "'int'", "'float'", "'string'", 
                     "'table'", "'row'", "'column'", "'void'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "','", "'.'", "':'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "STRUCT", "EXTENDS", "IS", "METHOD", 
                      "END", "SUB", "REF", "IF", "ELSE", "FOR", "IN", "RETURN", 
                      "NEW", "TYPE_INT", "TYPE_FLOAT", "TYPE_STRING", "TYPE_TABLE", 
                      "TYPE_ROW", "TYPE_COLUMN", "TYPE_VOID", "ID", "INT", 
                      "FLOAT", "STRING", "COMMENT", "NL", "WS", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "COMMA", "DOT", "COLON", 
                      "ASSIGN", "PLUS", "MINUS", "STAR", "SLASH", "EQ", 
                      "NEQ", "GT", "LT", "GE", "LE" ]

    RULE_program = 0
    RULE_structDecl = 1
    RULE_memberDecl = 2
    RULE_methodDecl = 3
    RULE_subroutineDecl = 4
    RULE_paramList = 5
    RULE_param = 6
    RULE_statement = 7
    RULE_assignStmt = 8
    RULE_pathExpr = 9
    RULE_funcCallStmt = 10
    RULE_methodCallStmt = 11
    RULE_ifStmt = 12
    RULE_forStmt = 13
    RULE_returnStmt = 14
    RULE_expr = 15
    RULE_exprList = 16
    RULE_typeDecl = 17
    RULE_literal = 18

    ruleNames =  [ "program", "structDecl", "memberDecl", "methodDecl", 
                   "subroutineDecl", "paramList", "param", "statement", 
                   "assignStmt", "pathExpr", "funcCallStmt", "methodCallStmt", 
                   "ifStmt", "forStmt", "returnStmt", "expr", "exprList", 
                   "typeDecl", "literal" ]

    EOF = Token.EOF
    STRUCT=1
    EXTENDS=2
    IS=3
    METHOD=4
    END=5
    SUB=6
    REF=7
    IF=8
    ELSE=9
    FOR=10
    IN=11
    RETURN=12
    NEW=13
    TYPE_INT=14
    TYPE_FLOAT=15
    TYPE_STRING=16
    TYPE_TABLE=17
    TYPE_ROW=18
    TYPE_COLUMN=19
    TYPE_VOID=20
    ID=21
    INT=22
    FLOAT=23
    STRING=24
    COMMENT=25
    NL=26
    WS=27
    LPAREN=28
    RPAREN=29
    LBRACE=30
    RBRACE=31
    COMMA=32
    DOT=33
    COLON=34
    ASSIGN=35
    PLUS=36
    MINUS=37
    STAR=38
    SLASH=39
    EQ=40
    NEQ=41
    GT=42
    LT=43
    GE=44
    LE=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RelationalLangParser.EOF, 0)

        def structDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.StructDeclContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.StructDeclContext,i)


        def subroutineDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.SubroutineDeclContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.SubroutineDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.StatementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.NL)
            else:
                return self.getToken(RelationalLangParser.NL, i)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RelationalLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1440757058) != 0):
                self.state = 42
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 38
                    self.structDecl()
                    pass
                elif token in [6]:
                    self.state = 39
                    self.subroutineDecl()
                    pass
                elif token in [8, 10, 12, 13, 21, 22, 23, 24, 28, 30]:
                    self.state = 40
                    self.statement()
                    pass
                elif token in [26]:
                    self.state = 41
                    self.match(RelationalLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(RelationalLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.STRUCT)
            else:
                return self.getToken(RelationalLangParser.STRUCT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.ID)
            else:
                return self.getToken(RelationalLangParser.ID, i)

        def IS(self):
            return self.getToken(RelationalLangParser.IS, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.NL)
            else:
                return self.getToken(RelationalLangParser.NL, i)

        def END(self):
            return self.getToken(RelationalLangParser.END, 0)

        def EXTENDS(self):
            return self.getToken(RelationalLangParser.EXTENDS, 0)

        def memberDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.MemberDeclContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.MemberDeclContext,i)


        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.MethodDeclContext,i)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_structDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = RelationalLangParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(RelationalLangParser.STRUCT)
            self.state = 50
            self.match(RelationalLangParser.ID)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 51
                self.match(RelationalLangParser.EXTENDS)
                self.state = 52
                self.match(RelationalLangParser.ID)


            self.state = 55
            self.match(RelationalLangParser.IS)
            self.state = 56
            self.match(RelationalLangParser.NL)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 69206032) != 0):
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [21]:
                    self.state = 57
                    self.memberDecl()
                    pass
                elif token in [4]:
                    self.state = 58
                    self.methodDecl()
                    pass
                elif token in [26]:
                    self.state = 59
                    self.match(RelationalLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(RelationalLangParser.END)
            self.state = 66
            self.match(RelationalLangParser.STRUCT)
            self.state = 67
            self.match(RelationalLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def COLON(self):
            return self.getToken(RelationalLangParser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(RelationalLangParser.TypeDeclContext,0)


        def NL(self):
            return self.getToken(RelationalLangParser.NL, 0)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_memberDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberDecl" ):
                return visitor.visitMemberDecl(self)
            else:
                return visitor.visitChildren(self)




    def memberDecl(self):

        localctx = RelationalLangParser.MemberDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memberDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(RelationalLangParser.ID)
            self.state = 70
            self.match(RelationalLangParser.COLON)
            self.state = 71
            self.typeDecl()
            self.state = 72
            self.match(RelationalLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METHOD(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.METHOD)
            else:
                return self.getToken(RelationalLangParser.METHOD, i)

        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.NL)
            else:
                return self.getToken(RelationalLangParser.NL, i)

        def END(self):
            return self.getToken(RelationalLangParser.END, 0)

        def paramList(self):
            return self.getTypedRuleContext(RelationalLangParser.ParamListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.StatementContext,i)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = RelationalLangParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(RelationalLangParser.METHOD)
            self.state = 75
            self.match(RelationalLangParser.ID)
            self.state = 76
            self.match(RelationalLangParser.LPAREN)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4178048) != 0):
                self.state = 77
                self.paramList()


            self.state = 80
            self.match(RelationalLangParser.RPAREN)
            self.state = 81
            self.match(RelationalLangParser.NL)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1440756992) != 0):
                self.state = 84
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 10, 12, 13, 21, 22, 23, 24, 28, 30]:
                    self.state = 82
                    self.statement()
                    pass
                elif token in [26]:
                    self.state = 83
                    self.match(RelationalLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(RelationalLangParser.END)
            self.state = 90
            self.match(RelationalLangParser.METHOD)
            self.state = 91
            self.match(RelationalLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubroutineDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.SUB)
            else:
                return self.getToken(RelationalLangParser.SUB, i)

        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.NL)
            else:
                return self.getToken(RelationalLangParser.NL, i)

        def END(self):
            return self.getToken(RelationalLangParser.END, 0)

        def paramList(self):
            return self.getTypedRuleContext(RelationalLangParser.ParamListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.StatementContext,i)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_subroutineDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubroutineDecl" ):
                return visitor.visitSubroutineDecl(self)
            else:
                return visitor.visitChildren(self)




    def subroutineDecl(self):

        localctx = RelationalLangParser.SubroutineDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subroutineDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(RelationalLangParser.SUB)
            self.state = 94
            self.match(RelationalLangParser.ID)
            self.state = 95
            self.match(RelationalLangParser.LPAREN)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4178048) != 0):
                self.state = 96
                self.paramList()


            self.state = 99
            self.match(RelationalLangParser.RPAREN)
            self.state = 100
            self.match(RelationalLangParser.NL)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1440756992) != 0):
                self.state = 103
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 10, 12, 13, 21, 22, 23, 24, 28, 30]:
                    self.state = 101
                    self.statement()
                    pass
                elif token in [26]:
                    self.state = 102
                    self.match(RelationalLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(RelationalLangParser.END)
            self.state = 109
            self.match(RelationalLangParser.SUB)
            self.state = 110
            self.match(RelationalLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.COMMA)
            else:
                return self.getToken(RelationalLangParser.COMMA, i)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = RelationalLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.param()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 113
                self.match(RelationalLangParser.COMMA)
                self.state = 114
                self.param()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeDecl(self):
            return self.getTypedRuleContext(RelationalLangParser.TypeDeclContext,0)


        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def REF(self):
            return self.getToken(RelationalLangParser.REF, 0)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = RelationalLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 120
                self.match(RelationalLangParser.REF)


            self.state = 123
            self.typeDecl()
            self.state = 124
            self.match(RelationalLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(RelationalLangParser.AssignStmtContext,0)


        def NL(self):
            return self.getToken(RelationalLangParser.NL, 0)

        def funcCallStmt(self):
            return self.getTypedRuleContext(RelationalLangParser.FuncCallStmtContext,0)


        def methodCallStmt(self):
            return self.getTypedRuleContext(RelationalLangParser.MethodCallStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(RelationalLangParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(RelationalLangParser.ForStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(RelationalLangParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = RelationalLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.assignStmt()
                self.state = 127
                self.match(RelationalLangParser.NL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.funcCallStmt()
                self.state = 130
                self.match(RelationalLangParser.NL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.methodCallStmt()
                self.state = 133
                self.match(RelationalLangParser.NL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.ifStmt()
                self.state = 136
                self.match(RelationalLangParser.NL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 138
                self.forStmt()
                self.state = 139
                self.match(RelationalLangParser.NL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.returnStmt()
                self.state = 142
                self.match(RelationalLangParser.NL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathExpr(self):
            return self.getTypedRuleContext(RelationalLangParser.PathExprContext,0)


        def ASSIGN(self):
            return self.getToken(RelationalLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = RelationalLangParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.pathExpr()
            self.state = 147
            self.match(RelationalLangParser.ASSIGN)
            self.state = 148
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.ID)
            else:
                return self.getToken(RelationalLangParser.ID, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.DOT)
            else:
                return self.getToken(RelationalLangParser.DOT, i)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_pathExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathExpr" ):
                return visitor.visitPathExpr(self)
            else:
                return visitor.visitChildren(self)




    def pathExpr(self):

        localctx = RelationalLangParser.PathExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pathExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(RelationalLangParser.ID)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 151
                    self.match(RelationalLangParser.DOT)
                    self.state = 152
                    self.match(RelationalLangParser.ID) 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)

        def exprList(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprListContext,0)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_funcCallStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallStmt" ):
                return visitor.visitFuncCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def funcCallStmt(self):

        localctx = RelationalLangParser.FuncCallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCallStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(RelationalLangParser.ID)
            self.state = 159
            self.match(RelationalLangParser.LPAREN)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1373642752) != 0):
                self.state = 160
                self.exprList()


            self.state = 163
            self.match(RelationalLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(RelationalLangParser.DOT, 0)

        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)

        def exprList(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprListContext,0)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_methodCallStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallStmt" ):
                return visitor.visitMethodCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def methodCallStmt(self):

        localctx = RelationalLangParser.MethodCallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_methodCallStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expr(0)
            self.state = 166
            self.match(RelationalLangParser.DOT)
            self.state = 167
            self.match(RelationalLangParser.ID)
            self.state = 168
            self.match(RelationalLangParser.LPAREN)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1373642752) != 0):
                self.state = 169
                self.exprList()


            self.state = 172
            self.match(RelationalLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.IF)
            else:
                return self.getToken(RelationalLangParser.IF, i)

        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.COLON)
            else:
                return self.getToken(RelationalLangParser.COLON, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.NL)
            else:
                return self.getToken(RelationalLangParser.NL, i)

        def END(self):
            return self.getToken(RelationalLangParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(RelationalLangParser.ELSE, 0)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = RelationalLangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(RelationalLangParser.IF)
            self.state = 175
            self.expr(0)
            self.state = 176
            self.match(RelationalLangParser.COLON)
            self.state = 177
            self.match(RelationalLangParser.NL)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1440756992) != 0):
                self.state = 180
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 10, 12, 13, 21, 22, 23, 24, 28, 30]:
                    self.state = 178
                    self.statement()
                    pass
                elif token in [26]:
                    self.state = 179
                    self.match(RelationalLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 185
                self.match(RelationalLangParser.ELSE)
                self.state = 186
                self.match(RelationalLangParser.COLON)
                self.state = 187
                self.match(RelationalLangParser.NL)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1440756992) != 0):
                    self.state = 190
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8, 10, 12, 13, 21, 22, 23, 24, 28, 30]:
                        self.state = 188
                        self.statement()
                        pass
                    elif token in [26]:
                        self.state = 189
                        self.match(RelationalLangParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 197
            self.match(RelationalLangParser.END)
            self.state = 198
            self.match(RelationalLangParser.IF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.FOR)
            else:
                return self.getToken(RelationalLangParser.FOR, i)

        def typeDecl(self):
            return self.getTypedRuleContext(RelationalLangParser.TypeDeclContext,0)


        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def IN(self):
            return self.getToken(RelationalLangParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(RelationalLangParser.COLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.NL)
            else:
                return self.getToken(RelationalLangParser.NL, i)

        def END(self):
            return self.getToken(RelationalLangParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.StatementContext,i)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = RelationalLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(RelationalLangParser.FOR)
            self.state = 201
            self.typeDecl()
            self.state = 202
            self.match(RelationalLangParser.ID)
            self.state = 203
            self.match(RelationalLangParser.IN)
            self.state = 204
            self.expr(0)
            self.state = 205
            self.match(RelationalLangParser.COLON)
            self.state = 206
            self.match(RelationalLangParser.NL)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1440756992) != 0):
                self.state = 209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 10, 12, 13, 21, 22, 23, 24, 28, 30]:
                    self.state = 207
                    self.statement()
                    pass
                elif token in [26]:
                    self.state = 208
                    self.match(RelationalLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(RelationalLangParser.END)
            self.state = 215
            self.match(RelationalLangParser.FOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(RelationalLangParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)


        def getRuleIndex(self):
            return RelationalLangParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = RelationalLangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(RelationalLangParser.RETURN)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1373642752) != 0):
                self.state = 218
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RelationalLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RowLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(RelationalLangParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(RelationalLangParser.RBRACE, 0)
        def exprList(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRowLiteral" ):
                return visitor.visitRowLiteral(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.ExprContext,i)

        def STAR(self):
            return self.getToken(RelationalLangParser.STAR, 0)
        def SLASH(self):
            return self.getToken(RelationalLangParser.SLASH, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pathExpr(self):
            return self.getTypedRuleContext(RelationalLangParser.PathExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompareExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(RelationalLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(RelationalLangParser.NEQ, 0)
        def GT(self):
            return self.getToken(RelationalLangParser.GT, 0)
        def LT(self):
            return self.getToken(RelationalLangParser.LT, 0)
        def GE(self):
            return self.getToken(RelationalLangParser.GE, 0)
        def LE(self):
            return self.getToken(RelationalLangParser.LE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)


    class CastExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)
        def typeDecl(self):
            return self.getTypedRuleContext(RelationalLangParser.TypeDeclContext,0)

        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpr" ):
                return visitor.visitCastExpr(self)
            else:
                return visitor.visitChildren(self)


    class NewExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(RelationalLangParser.NEW, 0)
        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)
        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewExpr" ):
                return visitor.visitNewExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(RelationalLangParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(RelationalLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(RelationalLangParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)
        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RelationalLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprContext,0)

        def DOT(self):
            return self.getToken(RelationalLangParser.DOT, 0)
        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)
        def LPAREN(self):
            return self.getToken(RelationalLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(RelationalLangParser.RPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(RelationalLangParser.ExprListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallExpr" ):
                return visitor.visitMethodCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RelationalLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = RelationalLangParser.CastExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 222
                self.match(RelationalLangParser.LPAREN)
                self.state = 223
                self.typeDecl()
                self.state = 224
                self.match(RelationalLangParser.RPAREN)
                self.state = 225
                self.expr(11)
                pass

            elif la_ == 2:
                localctx = RelationalLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 227
                self.pathExpr()
                pass

            elif la_ == 3:
                localctx = RelationalLangParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 228
                self.literal()
                pass

            elif la_ == 4:
                localctx = RelationalLangParser.RowLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 229
                self.match(RelationalLangParser.LBRACE)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1373642752) != 0):
                    self.state = 230
                    self.exprList()


                self.state = 233
                self.match(RelationalLangParser.RBRACE)
                pass

            elif la_ == 5:
                localctx = RelationalLangParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 234
                self.match(RelationalLangParser.ID)
                self.state = 235
                self.match(RelationalLangParser.LPAREN)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1373642752) != 0):
                    self.state = 236
                    self.exprList()


                self.state = 239
                self.match(RelationalLangParser.RPAREN)
                pass

            elif la_ == 6:
                localctx = RelationalLangParser.NewExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 240
                self.match(RelationalLangParser.NEW)
                self.state = 241
                self.match(RelationalLangParser.ID)
                self.state = 242
                self.match(RelationalLangParser.LPAREN)
                self.state = 243
                self.match(RelationalLangParser.RPAREN)
                pass

            elif la_ == 7:
                localctx = RelationalLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 244
                self.match(RelationalLangParser.LPAREN)
                self.state = 245
                self.expr(0)
                self.state = 246
                self.match(RelationalLangParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 267
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = RelationalLangParser.MulDivExprContext(self, RelationalLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 250
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 251
                        _la = self._input.LA(1)
                        if not(_la==38 or _la==39):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 252
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = RelationalLangParser.AddSubExprContext(self, RelationalLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 253
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 254
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==37):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 255
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = RelationalLangParser.CompareExprContext(self, RelationalLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 256
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 257
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69269232549888) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 258
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = RelationalLangParser.MethodCallExprContext(self, RelationalLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 259
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 260
                        self.match(RelationalLangParser.DOT)
                        self.state = 261
                        self.match(RelationalLangParser.ID)
                        self.state = 262
                        self.match(RelationalLangParser.LPAREN)
                        self.state = 264
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1373642752) != 0):
                            self.state = 263
                            self.exprList()


                        self.state = 266
                        self.match(RelationalLangParser.RPAREN)
                        pass

             
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RelationalLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RelationalLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RelationalLangParser.COMMA)
            else:
                return self.getToken(RelationalLangParser.COMMA, i)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = RelationalLangParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.expr(0)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 273
                self.match(RelationalLangParser.COMMA)
                self.state = 274
                self.expr(0)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(RelationalLangParser.TYPE_INT, 0)

        def TYPE_FLOAT(self):
            return self.getToken(RelationalLangParser.TYPE_FLOAT, 0)

        def TYPE_STRING(self):
            return self.getToken(RelationalLangParser.TYPE_STRING, 0)

        def TYPE_TABLE(self):
            return self.getToken(RelationalLangParser.TYPE_TABLE, 0)

        def TYPE_ROW(self):
            return self.getToken(RelationalLangParser.TYPE_ROW, 0)

        def TYPE_COLUMN(self):
            return self.getToken(RelationalLangParser.TYPE_COLUMN, 0)

        def TYPE_VOID(self):
            return self.getToken(RelationalLangParser.TYPE_VOID, 0)

        def ID(self):
            return self.getToken(RelationalLangParser.ID, 0)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = RelationalLangParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4177920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RelationalLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(RelationalLangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(RelationalLangParser.STRING, 0)

        def getRuleIndex(self):
            return RelationalLangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = RelationalLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




