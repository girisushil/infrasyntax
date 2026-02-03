// A correct, combined grammar for Dockerfile
grammar dk;

dockerfile : instruction* EOF;

instruction
    : (from | run | cmd | label | maintainer | expose | env | add | copy | entrypoint | volume | user | workdir | arg | onbuild | stopsignal | healthcheck | shell) NEWLINE
    | COMMENT NEWLINE
    | NEWLINE // Allow empty lines
    ;

from : FROM (platform_opt)? image_spec (as_opt)? (name_opt)? ;
run : RUN (json_command | shell_command) ;
cmd : CMD (json_command | shell_command) ;
label : LABEL label_pair (label_pair)* ;
maintainer : MAINTAINER ANY_CHAR_EXCEPT_NEWLINE+ ;
expose : EXPOSE WORD (WORD)* ;
env : ENV (env_pair | env_single) ;
add : ADD (param_opt)* path_spec path_spec ;
copy : COPY (param_opt)* path_spec path_spec ;
entrypoint : ENTRYPOINT (json_command | shell_command) ;
volume : VOLUME (json_array | shell_command_paths) ;
user : USER (WORD | (WORD ':' WORD)) ;
workdir : WORKDIR path_spec ;
arg : ARG (WORD | WORD '=' (WORD | QUOTED_STRING)) ;
onbuild : ONBUILD instruction ;
stopsignal : STOPSIGNAL WORD ;
healthcheck : HEALTHCHECK (health_none | health_cmd) ;
shell : SHELL json_array ;

// --- Sub-rules ---

platform_opt : PLATFORM WORD ;
as_opt : AS WORD ;
name_opt : NAME EQ WORD ;
param_opt : (CHOWN | CHMOD | FROM) EQ (WORD | (WORD ':' WORD)) ;
image_spec : WORD (':' WORD)? ('@' WORD ':' WORD)? ;
label_pair : WORD EQ (WORD | QUOTED_STRING) ;
env_pair : WORD EQ (WORD | QUOTED_STRING) ;
env_single : WORD (WORD | QUOTED_STRING) ;
path_spec : (WORD | QUOTED_STRING | TILDE | POINT | RSLASH | DOLLAR | ASTERISK | MINUS | UNDERSCORE)+ ;
shell_command_paths : path_spec (path_spec)* ;
json_command : LBRACKET QUOTED_STRING (COMMA QUOTED_STRING)* RBRACKET ;
json_array : LBRACKET QUOTED_STRING (COMMA QUOTED_STRING)* RBRACKET ;
shell_command : ANY_CHAR_EXCEPT_NEWLINE+ ;
health_none : NONE ;
health_cmd : (options_opt)* CMD (json_command | shell_command) ;
options_opt : (INTERVAL | TIMEOUT | START_PERIOD | RETRIES) EQ (INTEGER) ('s' | 'ms' | 'm') ;

// --- Lexer Rules (Tokens) ---

// Keywords
FROM : 'from' | 'FROM' ;
RUN : 'run' | 'RUN' ;
CMD : 'cmd' | 'CMD' ;
LABEL : 'label' | 'LABEL' ;
MAINTAINER : 'maintainer' | 'MAINTAINER' ;
EXPOSE : 'expose' | 'EXPOSE' ;
ENV : 'env' | 'ENV' ;
ADD : 'add' | 'ADD' ;
COPY : 'copy' | 'COPY' ;
ENTRYPOINT : 'entrypoint' | 'ENTRYPOINT' ;
VOLUME : 'volume' | 'VOLUME' ;
USER : 'user' | 'USER' ;
WORKDIR : 'workdir' | 'WORKDIR' ;
ARG : 'arg' | 'ARG' ;
ONBUILD : 'onbuild' | 'ONBUILD' ;
STOPSIGNAL : 'stopsignal' | 'STOPSIGNAL' ;
HEALTHCHECK : 'healthcheck' | 'HEALTHCHECK' ;
SHELL : 'shell' | 'SHELL' ;
NONE : 'none' | 'NONE' ;
AS : 'as' | 'AS' ;
NAME : 'name' | 'NAME' ;
CHOWN : '--chown' ;
CHMOD : '--chmod' ;
PLATFORM : '--platform' ;
INTERVAL : '--interval' ;
TIMEOUT : '--timeout' ;
START_PERIOD : '--start-period' ;
RETRIES : '--retries' ;

// Primitives
COMMENT : HASH ANY_CHAR_EXCEPT_NEWLINE* ;
NEWLINE : ( '\r' '\n'? | '\n' ) ;
WORD : ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' | '-' | '$' | '{' | '}' | ':' | '/' )+ ;
INTEGER : ( '0-" .. "9' )+ ;
QUOTED_STRING : '"' ( ~'"' )*? '"' ;

// Symbols
LBRACKET : '[' ;
RBRACKET : ']' ;
EQ : '=' ;
COMMA : ',' ;
HASH : '#' ;
RSLASH : '/' ;
ASTERISK : '*' ;
DOLLAR : '$' ;
POINT : '.' ;
MINUS : '-' ;
UNDERSCORE : '_' ;
TILDE : '~' ;

// Catch-all
ANY_CHAR_EXCEPT_NEWLINE : ~'\n' ;

// Whitespace
WS : ( ' ' | '\t' )+ -> skip ;
LINE_CONTINUATION : '\\' NEWLINE -> skip ;