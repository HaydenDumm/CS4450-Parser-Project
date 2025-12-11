grammar ParserProject03;

//-------------- Parser --------------

// PROG: Allow statements separated by newlines.
// The (stmt NL+)* handles all lines except the last one.
// The stmt? handles the potential last line (which might satisfy EOF directly).
prog
    : NL* (stmt NL+)* stmt? NL* EOF
    ;

stmt
    : simpleAssign      #AssignStmt
    | augAssign         #AugAssignStmt
    | if_stmt           #IfLogicStmt
    | while_stmt        #WhileStmt
    | for_stmt          #ForStmt
    ;

// BLOCK: Similar to prog, it's a list of statements.
// It consumes statements separated by newlines until it hits a keyword (like else) or EOF.
block
    : stmt (NL+ stmt)* NL*
    ;

// --- Control Flow ---
if_stmt
    : IF expr ':' NL block
      (ELIF expr ':' NL block)*
      (ELSE ':' NL block)?
    ;

while_stmt
    : WHILE expr ':' NL block
    ;

for_stmt
    : FOR IDENT IN expr ':' NL block
    ;

// --- Assignments ---
simpleAssign
    : IDENT '=' expr
    ;

augAssign
    : IDENT augOp expr
    ;

augOp
    : '+=' | '-=' | '*=' | '/='
    ;

// --- Expressions ---
expr
    : '-' expr                           #UnaryMinus
    | '+' expr                           #UnaryPlus
    | expr ('*'|'/'|'%') expr            #MulDivMod
    | expr ('+'|'-') expr                #AddSub
    | expr ('>'|'<'|'>='|'<='|'=='|'!=') expr #Comparison
    | NOT expr                           #NotLogic
    | expr AND expr                      #AndLogic
    | expr OR expr                       #OrLogic
    | primary                            #Atom
    ;

primary
    : literal
    | listLiteral
    | IDENT '(' (expr (',' expr)*)? ')'
    | IDENT
    | '(' expr ')'
    ;

listLiteral
    : '[' (expr (',' expr)*)? ']'
    ;

literal
    : boolean_val
    | NUMBER
    | STRING
    ;

boolean_val
    : TRUE
    | FALSE
    ;

//-------------- Lexer --------------

// --- Keywords ---
IF      : 'if';
ELIF    : 'elif';
ELSE    : 'else';
TRUE    : 'True';
FALSE   : 'False';
AND     : 'and';
OR      : 'or';
NOT     : 'not';
FOR     : 'for';
IN      : 'in';
WHILE   : 'while';

// --- Literals ---
NUMBER
    : DIGIT+ '.' DIGIT*
    | '.' DIGIT+
    | DIGIT+
    ;

STRING
    : '"'  ( ~["\\]  | '\\' . )* '"'
    | '\'' ( ~['\\]  | '\\' . )* '\''
    ;

// --- Identifiers ---
IDENT
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// --- Separators & Whitespace ---
BLOCK_COMMENT
    : '\'\'\'' ( . | '\r' | '\n' )*? '\'\'\'' -> skip
    ;


LINE_COMMENT
    : '#' ~[\r\n]* -> skip
    ;

NL
    : '\r'? '\n'
    ;

WS
    : [ \t]+ -> skip
    ;

fragment DIGIT : [0-9];