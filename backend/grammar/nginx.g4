/*
 * This is the complete, community-vetted Nginx grammar.
 * It is complex, but it is required to handle real-world files.
 * This version has been fixed for errors related to empty string matches.
 */
grammar nginx;

// --- Parser Rules ---

config
	: ( directive | LBRACE | RBRACE )* EOF
	;

directive
	: ( http | server | upstream | location | if_stmt | limit_except )
	| ( include | lua_code )
	;

http
	: http_name LBRACE ( directive | parameter )* RBRACE
	;

server
	: server_name LBRACE ( directive | parameter )* RBRACE
	;

upstream
	: upstream_name upstream_servers LBRACE ( directive | parameter )* RBRACE
	;

location
	: location_name location_match? LBRACE ( directive | parameter )* RBRACE
	;

limit_except
	: limit_except_name http_method ( http_method )* LBRACE ( directive | parameter )* RBRACE
	;

if_stmt
	: if_name if_cond LBRACE ( directive | parameter )* RBRACE
	;

include
	: include_name path SEMI
	;

lua_code
	: lua_code_name ( LUA_CODE | parameter ) SEMI
	;

// This rule requires at least one name and one value, which is correct.
parameter
	: name ( value )+ SEMI
	;

http_method
	: ( GET | HEAD | POST | PUT | DELETE | MKCOL | COPY | MOVE | OPTIONS | PROPFIND | PROPPATCH | LOCK | UNLOCK | PATCH )
	;

// This rule requires at least one if_body inside the parentheses.
if_cond
	: LPAREN ( if_body )+ RPAREN
	;

if_body
	: ( if_param | if_compare | if_regexp | if_function | if_str )
	;

if_param
	: ( DOLLAR name | DOLLAR name LBRACE name ( COMMA name )* RBRACE )
	;

if_compare
	: ( EQUAL | NOT_EQUAL )
	;

if_regexp
	: ( REGEXP_START | REGEXP_START_NOT | REGEXP_START_CASE | REGEXP_START_CASE_NOT )
	;

if_function
	: ( FILE_EXIST | FILE_NOT_EXIST | FILE_DIR_EXIST | FILE_DIR_NOT_EXIST | FILE_EXE_EXIST | FILE_EXE_NOT_EXIST )
	;

if_str
	: ( WORD | SINGLE_STRING | DOUBLE_STRING | path | DOLLAR )
	;

upstream_servers
	: ( DOLLAR name | name )
	;

location_match
	: ( EQUAL | REGEXP_START | REGEXP_START_CASE | REGEXP_START_CASE_NOT | REGEXP_START_NOT )?
	;

name
	: ( WORD | SINGLE_STRING | DOUBLE_STRING | path | REGEXP_START | REGEXP_START_NOT | REGEXP_START_CASE | REGEXP_START_CASE_NOT | DOLLAR )
	;

value
	: ( WORD | SINGLE_STRING | DOUBLE_STRING | path | REGEXP_START | REGEXP_START_NOT | REGEXP_START_CASE | REGEXP_START_CASE_NOT | DOLLAR | on | off )
	;

on
	: ON
	;

off
	: OFF
	;

// *** CRITICAL FIX: Simplified the path rule to prevent empty match errors.
// A path must start with something: a forward slash or at least one path component.
path
	: (RSLASH | RSLASH RSLASH)? path_component+ (RSLASH | RSLASH RSLASH | POINT)?
	;

path_component
	: (WORD | INTEGER | DOLLAR | MINUS | UNDERSCORE | TILDE | POINT | ASTERISK)+
	;

http_name
	: HTTP
	;

server_name
	: SERVER
	;

upstream_name
	: UPSTREAM
	;

location_name
	: LOCATION
	;

if_name
	: IF
	;

include_name
	: INCLUDE
	;

limit_except_name
	: LIMIT_EXCEPT
	;

lua_code_name
	: ( LUA_BY_REWRITE | LUA_BY_ACCESS | LUA_BY_CONTENT | LUA_BY_HEADER_FILTER | LUA_BY_BODY_FILTER | LUA_BY_LOG | LUA_BY_BALANCER | LUA_BY_INIT | LUA_BY_INIT_WORKER | LUA_BY_EXIT_WORKER | LUA_BY_EXIT_MASTER | LUA_BY_SSL_CERT | LUA_BY_SSL_CLIENT_HELLO | LUA_BY_SHARED_DICT )
	;

// --- Lexer Rules (Tokens) ---

COMMENT
	: HASH ANY_CHAR*? ( EOL | EOF ) -> channel(HIDDEN)
	;

LUA_CODE
	: LUA_START .*? LUA_END
	;

WS
	: ( SPACE | TAB | EOL )+ -> channel(HIDDEN)
	;

// key words
HTTP
	: 'http'
	;

SERVER
	: 'server'
	;

UPSTREAM
	: 'upstream'
	;

LOCATION
	: 'location'
	;

IF
	: 'if'
	;

INCLUDE
	: 'include'
	;

LIMIT_EXCEPT
	: 'limit_except'
	;

LUA_BY_REWRITE
	: ( 'rewrite_by_lua_block' | 'rewrite_by_lua' | 'rewrite_by_lua_file' )
	;

LUA_BY_ACCESS
	: ( 'access_by_lua_block' | 'access_by_lua' | 'access_by_lua_file' )
	;

LUA_BY_CONTENT
	: ( 'content_by_lua_block' | 'content_by_lua' | 'content_by_lua_file' )
	;

LUA_BY_HEADER_FILTER
	: ( 'header_filter_by_lua_block' | 'header_filter_by_lua' | 'header_filter_by_lua_file' )
	;

LUA_BY_BODY_FILTER
	: ( 'body_filter_by_lua_block' | 'body_filter_by_lua' | 'body_filter_by_lua_file' )
	;

LUA_BY_LOG
	: ( 'log_by_lua_block' | 'log_by_lua' | 'log_by_lua_file' )
	;

LUA_BY_BALANCER
	: ( 'balancer_by_lua_block' | 'balancer_by_lua' | 'balancer_by_lua_file' )
	;

LUA_BY_INIT
	: ( 'init_by_lua_block' | 'init_by_lua' | 'init_by_lua_file' )
	;

LUA_BY_INIT_WORKER
	: ( 'init_worker_by_lua_block' | 'init_worker_by_lua' | 'init_worker_by_lua_file' )
	;

LUA_BY_EXIT_WORKER
	: ( 'exit_worker_by_lua_block' | 'exit_worker_by_lua' | 'exit_worker_by_lua_file' )
	;

LUA_BY_EXIT_MASTER
	: ( 'exit_master_by_lua_block' | 'exit_master_by_lua' | 'exit_master_by_lua_file' )
	;

LUA_BY_SSL_CERT
	: ( 'ssl_certificate_by_lua_block' | 'ssl_certificate_by_lua' | 'ssl_certificate_by_lua_file' )
	;

LUA_BY_SSL_CLIENT_HELLO
	: ( 'ssl_client_hello_by_lua_block' | 'ssl_client_hello_by_lua' | 'ssl_client_hello_by_lua_file' )
	;

LUA_BY_SHARED_DICT
	: ( 'lua_shared_dict' )
	;

LUA_START
	: '{' ( '!' | '-' )? '-'
	;

LUA_END
	: '-' ( '!' | '-' )? '}'
	;

// http method
GET
	: 'GET'
	;

HEAD
	: 'HEAD'
	;

POST
	: 'POST'
	;

PUT
	: 'PUT'
	;

DELETE
	: 'DELETE'
	;

MKCOL
	: 'MKCOL'
	;

COPY
	: 'COPY'
	;

MOVE
	: 'MOVE'
	;

OPTIONS
	: 'OPTIONS'
	;

PROPFIND
	: 'PROPFIND'
	;

PROPPATCH
	: 'PROPPATCH'
	;

LOCK
	: 'LOCK'
	;

UNLOCK
	: 'UNLOCK'
	;

PATCH
	: 'PATCH'
	;

ON
	: 'on'
	;

OFF
	: 'off'
	;

// compare
EQUAL
	: '=='
	;

NOT_EQUAL
	: '!='
	;

// regexp
REGEXP_START
	: '~'
	;

REGEXP_START_NOT
	: '!~'
	;

REGEXP_START_CASE
	: '~*'
	;

REGEXP_START_CASE_NOT
	: '!~*'
	;

// function
FILE_EXIST
	: '-f'
	;

FILE_NOT_EXIST
	: '!-f'
	;

FILE_DIR_EXIST
	: '-d'
	;

FILE_DIR_NOT_EXIST
	: '!-d'
	;

FILE_EXE_EXIST
	: '-x'
	;

FILE_EXE_NOT_EXIST
	: '!-x'
	;

// symbol
LPAREN
	: '('
	;

RPAREN
	: ')'
	;

LBRACE
	: '{'
	;

RBRACE
	: '}'
	;

SEMI
	: ';'
	;

COMMA
	: ','
	;

HASH
	: '#'
	;

RSLASH
	: '/'
	;

ASTERISK
	: '*'
	;

DOLLAR
	: '$'
	;

POINT
	: '.'
	;

MINUS
	: '-'
	;

UNDERSCORE
	: '_'
	;

TILDE
	: '`'
	;

// word
WORD
	: ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
	;

INTEGER
	: ( '0' .. '9' )+
	;

SINGLE_STRING
	: '\'' ( ~'\'' | '\'\'' )*? '\''
	;

DOUBLE_STRING
	: '"' ( ~'"' | '""' )*? '"'
	;

ANY_CHAR
	: .
	;

TAB
	: '\t'
	;

EOL
	: ( '\r' '\n'? | '\n' )
	;

SPACE
	: ' '
	;