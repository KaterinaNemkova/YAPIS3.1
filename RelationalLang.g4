grammar RelationalLang;

// --- ПАРСЕР ---

program
    : (structDecl | subroutineDecl | statement | NL)* EOF
    ;

// --- Структуры ---
// struct Name is \n ... end struct \n
structDecl
    : 'struct' ID ('extends' ID)? 'is' NL
      (memberDecl | methodDecl | NL)*
      'end' 'struct' NL
    ;

memberDecl
    : ID ':' typeDecl NL
    ;

methodDecl
    : 'method' ID '(' paramList? ')' NL
      (statement | NL)*
      'end' 'method' NL
    ;

// --- Подпрограммы ---
subroutineDecl
    : 'sub' ID '(' paramList? ')' NL
      (statement | NL)*
      'end' 'sub' NL
    ;

paramList
    : param (',' param)*
    ;

param
    : 'ref'? typeDecl ID
    ;

statement
    : assignStmt NL
    | funcCallStmt NL
    | methodCallStmt NL
    | ifStmt NL
    | forStmt NL
    | returnStmt NL
    ;

assignStmt
    : pathExpr '=' expr
    ;

pathExpr
    : ID ('.' ID)*
    ;

funcCallStmt
    : ID '(' exprList? ')'
    ;

methodCallStmt
    : expr '.' ID '(' exprList? ')'
    ;

ifStmt
    : 'if' expr ':' NL
      (statement | NL)*
      ('else' ':' NL (statement | NL)*)?
      'end' 'if'
    ;

forStmt
    : 'for' typeDecl ID 'in' expr ':' NL
      (statement | NL)*
      'end' 'for'
    ;

returnStmt
    : 'return' expr?
    ;

// --- Выражения ---
expr
    : '(' typeDecl ')' expr              # CastExpr
    | pathExpr                           # IdExpr
    | literal                            # LiteralExpr
    | '{' exprList? '}'                  # RowLiteral
    | ID '(' exprList? ')'               # FuncCallExpr
    | expr '.' ID '(' exprList? ')'      # MethodCallExpr
    | 'new' ID '(' ')'                   # NewExpr
    | expr ('*'|'/') expr                # MulDivExpr
    | expr ('+'|'-') expr                # AddSubExpr
    | expr ('=='|'!='|'>'|'<'|'>='|'<=') expr # CompareExpr
    | '(' expr ')'                       # ParenExpr
    ;

exprList
    : expr (',' expr)*
    ;

typeDecl
    : 'int' | 'float' | 'string' | 'table' | 'row' | 'column' | 'void' | ID
    ;

literal
    : INT | FLOAT | STRING
    ;

// --- ЛЕКСЕР ---

STRUCT: 'struct';
EXTENDS: 'extends';
IS: 'is';
METHOD: 'method';
END: 'end';
SUB: 'sub';
REF: 'ref';
IF: 'if';
ELSE: 'else';
FOR: 'for';
IN: 'in';
RETURN: 'return';
NEW: 'new';

TYPE_INT: 'int';
TYPE_FLOAT: 'float';
TYPE_STRING: 'string';
TYPE_TABLE: 'table';
TYPE_ROW: 'row';
TYPE_COLUMN: 'column';
TYPE_VOID: 'void';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';

COMMENT: '//' ~[\r\n]* -> skip;

NL: [\r\n]+;

WS: [ \t]+ -> skip;

LPAREN: '('; RPAREN: ')';
LBRACE: '{'; RBRACE: '}';
COMMA: ','; DOT: '.';
COLON: ':';
ASSIGN: '=';
PLUS: '+'; MINUS: '-'; STAR: '*'; SLASH: '/';
EQ: '=='; NEQ: '!='; GT: '>'; LT: '<'; GE: '>='; LE: '<=';