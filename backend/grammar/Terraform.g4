// A pure ANTLR4 grammar for Terraform's HCL syntax
grammar Terraform;

file : (block | statement)* EOF;

// FIXED: Replaced 'name' with 'WORD'
statement : WORD EQ (value | list) NEWLINE;

// FIXED: Replaced 'name' with 'WORD'
block : WORD (STRING | WORD)* LBRACE body RBRACE NEWLINE?;

body : (statement | block)*;

list : LBRACKET (value (COMMA value)*)? RBRACKET;

value :
    STRING
    | INTEGER
    | FLOAT
    | BOOL
    | WORD // For variable references like 'var.name'
    ;

// --- Lexer Rules (Tokens) ---

COMMENT : (HASH | RSLASH RSLASH) ANY_CHAR_EXCEPT_NEWLINE* NEWLINE? -> channel(HIDDEN);
MULTILINE_COMMENT : RSLASH ASTERISK .*? ASTERISK RSLASH -> channel(HIDDEN);

LBRACE : '{';
RBRACE : '}';
LBRACKET : '[';
RBRACKET : ']';
EQ : '=';
COMMA : ',';
HASH : '#';
RSLASH : '/';
ASTERISK : '*';

STRING : '"' ( ~'"' )*? '"';
INTEGER : '-'? ( '0' .. '9' )+;
FLOAT : '-'? ( '0' .. '9' )+ '.' ( '0' .. '9' )+;
BOOL : 'true' | 'false';

// A WORD can be a name or a reference like 'var.name' or 'aws_instance.foo'
WORD : ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '-' )*;

NEWLINE : ( '\r' '\n'? | '\n' );
WS : ( ' ' | '\t' )+ -> skip;

// Catch-all for parts of values we might have missed
ANY_CHAR_EXCEPT_NEWLINE : ~'\n';