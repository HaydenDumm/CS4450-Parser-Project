grammar ParserProject01;


//-------------- Parser --------------
prog
    : (NL* stmt)+ NL* EOF
    ;

stmt
    : simpleAssign NL*
    | augAssign    NL*
    ;

simpleAssign
    : IDENT '=' expr
    ;

augAssign
    : IDENT augOp expr
    ;

augOp
    : '+='
    | '-='
    | '*='
    | '/='
    ;

// precedence: unary -> * / % -> + -
expr
    : '-' expr                         #UnaryMinus
    | '+' expr                         #UnaryPlus
    | expr ('*'|'/'|'%') expr          #MulDivMod
    | expr ('+'|'-') expr              #AddSub
    | primary                          #Atom
    ;

primary
    : literal
    | listLiteral
    | IDENT
    | '(' expr ')'
    ;

listLiteral
    : '[' (expr (',' expr)*)? ']'
    ;

literal
    : BOOL
    | NUMBER
    | STRING
    ;

//-------------- Lexer --------------

NUMBER
    : DIGIT+ '.' DIGIT*        // 1. , 1.0 , 123.45
    | '.' DIGIT+               // .5
    | DIGIT+                   // 10
    ;

STRING
    : '"'  ( ~["\\]  | '\\' . )* '"'
    | '\'' ( ~['\\]  | '\\' . )* '\''
    ;

BOOL
    : 'True'
    | 'False'
    ;

IDENT
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// newline as statement separator
NL
    : '\r'? '\n'
    ;

// spaces/tabs
WS
    : [ \t]+ -> skip
    ;

fragment DIGIT : [0-9];
