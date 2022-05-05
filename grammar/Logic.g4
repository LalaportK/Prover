grammar Logic;

/*
=======================
    Parser
=======================
*/
top
    : logicalFormula EOF
    ;

logicalFormula
    : Identifier                         #AtomicFormula
    | LeftParenthesis logicalFormula RightParenthesis  #QuotedFormula
    | NegSymbol logicalFormula                   #Negation
    | logicalFormula OrSymbol logicalFormula   #Disjunction
    | logicalFormula AndSymbol logicalFormula   #Conjunction
    | logicalFormula ImplicationSymbol logicalFormula   #Implication
    ;

/*
=======================
    Lexer
=======================
*/

/* logical symbols */
ImplicationSymbol
    : '\\to'
    ;

AndSymbol
    : '\\land'
    ;

OrSymbol
    : '\\lor'
    ;

NegSymbol
    : '\\neg'
    ;

Identifier
    : [a-zA-Z]
    | [a-zA-Z] '_{' [0-9]+ '}'
    | [a-zA-Z] '_' [0-9]+
    ;

/* other symbols */
Delimiter
    : ','
    ;

LeftParenthesis
    : '('
    ;

RightParenthesis
    : ')'
    ;
WS
    : [ \n\t\r]+ -> skip
    ;