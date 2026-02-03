# Generated from ./backend/grammar/nginx.g4 by ANTLR 4.13.1
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
        4,1,76,312,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,5,0,74,8,0,10,0,12,0,77,9,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,87,8,1,1,1,1,1,3,1,91,8,1,3,1,93,8,1,1,
        2,1,2,1,2,1,2,5,2,99,8,2,10,2,12,2,102,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,5,3,110,8,3,10,3,12,3,113,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,
        122,8,4,10,4,12,4,125,9,4,1,4,1,4,1,5,1,5,3,5,131,8,5,1,5,1,5,1,
        5,5,5,136,8,5,10,5,12,5,139,9,5,1,5,1,5,1,6,1,6,1,6,5,6,146,8,6,
        10,6,12,6,149,9,6,1,6,1,6,1,6,5,6,154,8,6,10,6,12,6,157,9,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,5,7,166,8,7,10,7,12,7,169,9,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,180,8,9,1,9,1,9,1,10,1,10,4,10,186,
        8,10,11,10,12,10,187,1,10,1,10,1,11,1,11,1,12,1,12,4,12,196,8,12,
        11,12,12,12,197,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,207,8,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,217,8,14,10,14,12,14,
        220,9,14,1,14,1,14,3,14,224,8,14,1,15,1,15,1,16,1,16,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,3,18,237,8,18,1,19,1,19,1,19,3,19,242,8,19,
        1,20,3,20,245,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,256,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,3,22,269,8,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,3,25,278,8,
        25,1,25,4,25,281,8,25,11,25,12,25,282,1,25,1,25,1,25,1,25,3,25,289,
        8,25,1,26,4,26,292,8,26,11,26,12,26,293,1,27,1,27,1,28,1,28,1,29,
        1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,34,0,0,
        35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,0,7,1,0,27,40,1,0,43,44,1,
        0,45,48,1,0,49,54,2,0,43,43,45,48,1,0,63,70,1,0,11,24,340,0,75,1,
        0,0,0,2,92,1,0,0,0,4,94,1,0,0,0,6,105,1,0,0,0,8,116,1,0,0,0,10,128,
        1,0,0,0,12,142,1,0,0,0,14,160,1,0,0,0,16,172,1,0,0,0,18,176,1,0,
        0,0,20,183,1,0,0,0,22,191,1,0,0,0,24,193,1,0,0,0,26,206,1,0,0,0,
        28,223,1,0,0,0,30,225,1,0,0,0,32,227,1,0,0,0,34,229,1,0,0,0,36,236,
        1,0,0,0,38,241,1,0,0,0,40,244,1,0,0,0,42,255,1,0,0,0,44,268,1,0,
        0,0,46,270,1,0,0,0,48,272,1,0,0,0,50,277,1,0,0,0,52,291,1,0,0,0,
        54,295,1,0,0,0,56,297,1,0,0,0,58,299,1,0,0,0,60,301,1,0,0,0,62,303,
        1,0,0,0,64,305,1,0,0,0,66,307,1,0,0,0,68,309,1,0,0,0,70,74,3,2,1,
        0,71,74,5,57,0,0,72,74,5,58,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,
        1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,
        77,75,1,0,0,0,78,79,5,0,0,1,79,1,1,0,0,0,80,87,3,4,2,0,81,87,3,6,
        3,0,82,87,3,8,4,0,83,87,3,10,5,0,84,87,3,14,7,0,85,87,3,12,6,0,86,
        80,1,0,0,0,86,81,1,0,0,0,86,82,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,
        0,86,85,1,0,0,0,87,93,1,0,0,0,88,91,3,16,8,0,89,91,3,18,9,0,90,88,
        1,0,0,0,90,89,1,0,0,0,91,93,1,0,0,0,92,86,1,0,0,0,92,90,1,0,0,0,
        93,3,1,0,0,0,94,95,3,54,27,0,95,100,5,57,0,0,96,99,3,2,1,0,97,99,
        3,20,10,0,98,96,1,0,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,
        0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,58,
        0,0,104,5,1,0,0,0,105,106,3,56,28,0,106,111,5,57,0,0,107,110,3,2,
        1,0,108,110,3,20,10,0,109,107,1,0,0,0,109,108,1,0,0,0,110,113,1,
        0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,
        0,0,0,114,115,5,58,0,0,115,7,1,0,0,0,116,117,3,58,29,0,117,118,3,
        38,19,0,118,123,5,57,0,0,119,122,3,2,1,0,120,122,3,20,10,0,121,119,
        1,0,0,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,
        1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,5,58,0,0,127,9,1,
        0,0,0,128,130,3,60,30,0,129,131,3,40,20,0,130,129,1,0,0,0,130,131,
        1,0,0,0,131,132,1,0,0,0,132,137,5,57,0,0,133,136,3,2,1,0,134,136,
        3,20,10,0,135,133,1,0,0,0,135,134,1,0,0,0,136,139,1,0,0,0,137,135,
        1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,137,1,0,0,0,140,141,
        5,58,0,0,141,11,1,0,0,0,142,143,3,66,33,0,143,147,3,22,11,0,144,
        146,3,22,11,0,145,144,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,
        148,1,0,0,0,148,150,1,0,0,0,149,147,1,0,0,0,150,155,5,57,0,0,151,
        154,3,2,1,0,152,154,3,20,10,0,153,151,1,0,0,0,153,152,1,0,0,0,154,
        157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,158,1,0,0,0,157,
        155,1,0,0,0,158,159,5,58,0,0,159,13,1,0,0,0,160,161,3,62,31,0,161,
        162,3,24,12,0,162,167,5,57,0,0,163,166,3,2,1,0,164,166,3,20,10,0,
        165,163,1,0,0,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,
        167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,171,5,58,0,0,
        171,15,1,0,0,0,172,173,3,64,32,0,173,174,3,50,25,0,174,175,5,59,
        0,0,175,17,1,0,0,0,176,179,3,68,34,0,177,180,5,2,0,0,178,180,3,20,
        10,0,179,177,1,0,0,0,179,178,1,0,0,0,180,181,1,0,0,0,181,182,5,59,
        0,0,182,19,1,0,0,0,183,185,3,42,21,0,184,186,3,44,22,0,185,184,1,
        0,0,0,186,187,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,189,1,
        0,0,0,189,190,5,59,0,0,190,21,1,0,0,0,191,192,7,0,0,0,192,23,1,0,
        0,0,193,195,5,55,0,0,194,196,3,26,13,0,195,194,1,0,0,0,196,197,1,
        0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,199,1,0,0,0,199,200,5,
        56,0,0,200,25,1,0,0,0,201,207,3,28,14,0,202,207,3,30,15,0,203,207,
        3,32,16,0,204,207,3,34,17,0,205,207,3,36,18,0,206,201,1,0,0,0,206,
        202,1,0,0,0,206,203,1,0,0,0,206,204,1,0,0,0,206,205,1,0,0,0,207,
        27,1,0,0,0,208,209,5,64,0,0,209,224,3,42,21,0,210,211,5,64,0,0,211,
        212,3,42,21,0,212,213,5,57,0,0,213,218,3,42,21,0,214,215,5,60,0,
        0,215,217,3,42,21,0,216,214,1,0,0,0,217,220,1,0,0,0,218,216,1,0,
        0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,218,1,0,0,0,221,222,5,58,
        0,0,222,224,1,0,0,0,223,208,1,0,0,0,223,210,1,0,0,0,224,29,1,0,0,
        0,225,226,7,1,0,0,226,31,1,0,0,0,227,228,7,2,0,0,228,33,1,0,0,0,
        229,230,7,3,0,0,230,35,1,0,0,0,231,237,5,69,0,0,232,237,5,71,0,0,
        233,237,5,72,0,0,234,237,3,50,25,0,235,237,5,64,0,0,236,231,1,0,
        0,0,236,232,1,0,0,0,236,233,1,0,0,0,236,234,1,0,0,0,236,235,1,0,
        0,0,237,37,1,0,0,0,238,239,5,64,0,0,239,242,3,42,21,0,240,242,3,
        42,21,0,241,238,1,0,0,0,241,240,1,0,0,0,242,39,1,0,0,0,243,245,7,
        4,0,0,244,243,1,0,0,0,244,245,1,0,0,0,245,41,1,0,0,0,246,256,5,69,
        0,0,247,256,5,71,0,0,248,256,5,72,0,0,249,256,3,50,25,0,250,256,
        5,45,0,0,251,256,5,46,0,0,252,256,5,47,0,0,253,256,5,48,0,0,254,
        256,5,64,0,0,255,246,1,0,0,0,255,247,1,0,0,0,255,248,1,0,0,0,255,
        249,1,0,0,0,255,250,1,0,0,0,255,251,1,0,0,0,255,252,1,0,0,0,255,
        253,1,0,0,0,255,254,1,0,0,0,256,43,1,0,0,0,257,269,5,69,0,0,258,
        269,5,71,0,0,259,269,5,72,0,0,260,269,3,50,25,0,261,269,5,45,0,0,
        262,269,5,46,0,0,263,269,5,47,0,0,264,269,5,48,0,0,265,269,5,64,
        0,0,266,269,3,46,23,0,267,269,3,48,24,0,268,257,1,0,0,0,268,258,
        1,0,0,0,268,259,1,0,0,0,268,260,1,0,0,0,268,261,1,0,0,0,268,262,
        1,0,0,0,268,263,1,0,0,0,268,264,1,0,0,0,268,265,1,0,0,0,268,266,
        1,0,0,0,268,267,1,0,0,0,269,45,1,0,0,0,270,271,5,41,0,0,271,47,1,
        0,0,0,272,273,5,42,0,0,273,49,1,0,0,0,274,278,5,62,0,0,275,276,5,
        62,0,0,276,278,5,62,0,0,277,274,1,0,0,0,277,275,1,0,0,0,277,278,
        1,0,0,0,278,280,1,0,0,0,279,281,3,52,26,0,280,279,1,0,0,0,281,282,
        1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,288,1,0,0,0,284,289,
        5,62,0,0,285,286,5,62,0,0,286,289,5,62,0,0,287,289,5,65,0,0,288,
        284,1,0,0,0,288,285,1,0,0,0,288,287,1,0,0,0,288,289,1,0,0,0,289,
        51,1,0,0,0,290,292,7,5,0,0,291,290,1,0,0,0,292,293,1,0,0,0,293,291,
        1,0,0,0,293,294,1,0,0,0,294,53,1,0,0,0,295,296,5,4,0,0,296,55,1,
        0,0,0,297,298,5,5,0,0,298,57,1,0,0,0,299,300,5,6,0,0,300,59,1,0,
        0,0,301,302,5,7,0,0,302,61,1,0,0,0,303,304,5,8,0,0,304,63,1,0,0,
        0,305,306,5,9,0,0,306,65,1,0,0,0,307,308,5,10,0,0,308,67,1,0,0,0,
        309,310,7,6,0,0,310,69,1,0,0,0,34,73,75,86,90,92,98,100,109,111,
        121,123,130,135,137,147,153,155,165,167,179,187,197,206,218,223,
        236,241,244,255,268,277,282,288,293
    ]

class nginxParser ( Parser ):

    grammarFileName = "nginx.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'http'", "'server'", "'upstream'", "'location'", "'if'", 
                     "'include'", "'limit_except'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'GET'", "'HEAD'", "'POST'", 
                     "'PUT'", "'DELETE'", "'MKCOL'", "'COPY'", "'MOVE'", 
                     "'OPTIONS'", "'PROPFIND'", "'PROPPATCH'", "'LOCK'", 
                     "'UNLOCK'", "'PATCH'", "'on'", "'off'", "'=='", "'!='", 
                     "'~'", "'!~'", "'~*'", "'!~*'", "'-f'", "'!-f'", "'-d'", 
                     "'!-d'", "'-x'", "'!-x'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "'#'", "'/'", "'*'", "'$'", "'.'", "'-'", 
                     "'_'", "'`'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\t'", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "LUA_CODE", "WS", "HTTP", 
                      "SERVER", "UPSTREAM", "LOCATION", "IF", "INCLUDE", 
                      "LIMIT_EXCEPT", "LUA_BY_REWRITE", "LUA_BY_ACCESS", 
                      "LUA_BY_CONTENT", "LUA_BY_HEADER_FILTER", "LUA_BY_BODY_FILTER", 
                      "LUA_BY_LOG", "LUA_BY_BALANCER", "LUA_BY_INIT", "LUA_BY_INIT_WORKER", 
                      "LUA_BY_EXIT_WORKER", "LUA_BY_EXIT_MASTER", "LUA_BY_SSL_CERT", 
                      "LUA_BY_SSL_CLIENT_HELLO", "LUA_BY_SHARED_DICT", "LUA_START", 
                      "LUA_END", "GET", "HEAD", "POST", "PUT", "DELETE", 
                      "MKCOL", "COPY", "MOVE", "OPTIONS", "PROPFIND", "PROPPATCH", 
                      "LOCK", "UNLOCK", "PATCH", "ON", "OFF", "EQUAL", "NOT_EQUAL", 
                      "REGEXP_START", "REGEXP_START_NOT", "REGEXP_START_CASE", 
                      "REGEXP_START_CASE_NOT", "FILE_EXIST", "FILE_NOT_EXIST", 
                      "FILE_DIR_EXIST", "FILE_DIR_NOT_EXIST", "FILE_EXE_EXIST", 
                      "FILE_EXE_NOT_EXIST", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "SEMI", "COMMA", "HASH", "RSLASH", "ASTERISK", 
                      "DOLLAR", "POINT", "MINUS", "UNDERSCORE", "TILDE", 
                      "WORD", "INTEGER", "SINGLE_STRING", "DOUBLE_STRING", 
                      "ANY_CHAR", "TAB", "EOL", "SPACE" ]

    RULE_config = 0
    RULE_directive = 1
    RULE_http = 2
    RULE_server = 3
    RULE_upstream = 4
    RULE_location = 5
    RULE_limit_except = 6
    RULE_if_stmt = 7
    RULE_include = 8
    RULE_lua_code = 9
    RULE_parameter = 10
    RULE_http_method = 11
    RULE_if_cond = 12
    RULE_if_body = 13
    RULE_if_param = 14
    RULE_if_compare = 15
    RULE_if_regexp = 16
    RULE_if_function = 17
    RULE_if_str = 18
    RULE_upstream_servers = 19
    RULE_location_match = 20
    RULE_name = 21
    RULE_value = 22
    RULE_on = 23
    RULE_off = 24
    RULE_path = 25
    RULE_path_component = 26
    RULE_http_name = 27
    RULE_server_name = 28
    RULE_upstream_name = 29
    RULE_location_name = 30
    RULE_if_name = 31
    RULE_include_name = 32
    RULE_limit_except_name = 33
    RULE_lua_code_name = 34

    ruleNames =  [ "config", "directive", "http", "server", "upstream", 
                   "location", "limit_except", "if_stmt", "include", "lua_code", 
                   "parameter", "http_method", "if_cond", "if_body", "if_param", 
                   "if_compare", "if_regexp", "if_function", "if_str", "upstream_servers", 
                   "location_match", "name", "value", "on", "off", "path", 
                   "path_component", "http_name", "server_name", "upstream_name", 
                   "location_name", "if_name", "include_name", "limit_except_name", 
                   "lua_code_name" ]

    EOF = Token.EOF
    COMMENT=1
    LUA_CODE=2
    WS=3
    HTTP=4
    SERVER=5
    UPSTREAM=6
    LOCATION=7
    IF=8
    INCLUDE=9
    LIMIT_EXCEPT=10
    LUA_BY_REWRITE=11
    LUA_BY_ACCESS=12
    LUA_BY_CONTENT=13
    LUA_BY_HEADER_FILTER=14
    LUA_BY_BODY_FILTER=15
    LUA_BY_LOG=16
    LUA_BY_BALANCER=17
    LUA_BY_INIT=18
    LUA_BY_INIT_WORKER=19
    LUA_BY_EXIT_WORKER=20
    LUA_BY_EXIT_MASTER=21
    LUA_BY_SSL_CERT=22
    LUA_BY_SSL_CLIENT_HELLO=23
    LUA_BY_SHARED_DICT=24
    LUA_START=25
    LUA_END=26
    GET=27
    HEAD=28
    POST=29
    PUT=30
    DELETE=31
    MKCOL=32
    COPY=33
    MOVE=34
    OPTIONS=35
    PROPFIND=36
    PROPPATCH=37
    LOCK=38
    UNLOCK=39
    PATCH=40
    ON=41
    OFF=42
    EQUAL=43
    NOT_EQUAL=44
    REGEXP_START=45
    REGEXP_START_NOT=46
    REGEXP_START_CASE=47
    REGEXP_START_CASE_NOT=48
    FILE_EXIST=49
    FILE_NOT_EXIST=50
    FILE_DIR_EXIST=51
    FILE_DIR_NOT_EXIST=52
    FILE_EXE_EXIST=53
    FILE_EXE_NOT_EXIST=54
    LPAREN=55
    RPAREN=56
    LBRACE=57
    RBRACE=58
    SEMI=59
    COMMA=60
    HASH=61
    RSLASH=62
    ASTERISK=63
    DOLLAR=64
    POINT=65
    MINUS=66
    UNDERSCORE=67
    TILDE=68
    WORD=69
    INTEGER=70
    SINGLE_STRING=71
    DOUBLE_STRING=72
    ANY_CHAR=73
    TAB=74
    EOL=75
    SPACE=76

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ConfigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(nginxParser.EOF, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(nginxParser.DirectiveContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.LBRACE)
            else:
                return self.getToken(nginxParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.RBRACE)
            else:
                return self.getToken(nginxParser.RBRACE, i)

        def getRuleIndex(self):
            return nginxParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig" ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig" ):
                listener.exitConfig(self)




    def config(self):

        localctx = nginxParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 432345564261122032) != 0):
                self.state = 73
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 70
                    self.directive()
                    pass
                elif token in [57]:
                    self.state = 71
                    self.match(nginxParser.LBRACE)
                    pass
                elif token in [58]:
                    self.state = 72
                    self.match(nginxParser.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(nginxParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def http(self):
            return self.getTypedRuleContext(nginxParser.HttpContext,0)


        def server(self):
            return self.getTypedRuleContext(nginxParser.ServerContext,0)


        def upstream(self):
            return self.getTypedRuleContext(nginxParser.UpstreamContext,0)


        def location(self):
            return self.getTypedRuleContext(nginxParser.LocationContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(nginxParser.If_stmtContext,0)


        def limit_except(self):
            return self.getTypedRuleContext(nginxParser.Limit_exceptContext,0)


        def include(self):
            return self.getTypedRuleContext(nginxParser.IncludeContext,0)


        def lua_code(self):
            return self.getTypedRuleContext(nginxParser.Lua_codeContext,0)


        def getRuleIndex(self):
            return nginxParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)




    def directive(self):

        localctx = nginxParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_directive)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 80
                    self.http()
                    pass
                elif token in [5]:
                    self.state = 81
                    self.server()
                    pass
                elif token in [6]:
                    self.state = 82
                    self.upstream()
                    pass
                elif token in [7]:
                    self.state = 83
                    self.location()
                    pass
                elif token in [8]:
                    self.state = 84
                    self.if_stmt()
                    pass
                elif token in [10]:
                    self.state = 85
                    self.limit_except()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9]:
                    self.state = 88
                    self.include()
                    pass
                elif token in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 89
                    self.lua_code()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HttpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def http_name(self):
            return self.getTypedRuleContext(nginxParser.Http_nameContext,0)


        def LBRACE(self):
            return self.getToken(nginxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nginxParser.RBRACE, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(nginxParser.DirectiveContext,i)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.ParameterContext)
            else:
                return self.getTypedRuleContext(nginxParser.ParameterContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_http

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHttp" ):
                listener.enterHttp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHttp" ):
                listener.exitHttp(self)




    def http(self):

        localctx = nginxParser.HttpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_http)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.http_name()
            self.state = 95
            self.match(nginxParser.LBRACE)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611158252812501008) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 511) != 0):
                self.state = 98
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 96
                    self.directive()
                    pass
                elif token in [45, 46, 47, 48, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                    self.state = 97
                    self.parameter()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(nginxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def server_name(self):
            return self.getTypedRuleContext(nginxParser.Server_nameContext,0)


        def LBRACE(self):
            return self.getToken(nginxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nginxParser.RBRACE, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(nginxParser.DirectiveContext,i)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.ParameterContext)
            else:
                return self.getTypedRuleContext(nginxParser.ParameterContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_server

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServer" ):
                listener.enterServer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServer" ):
                listener.exitServer(self)




    def server(self):

        localctx = nginxParser.ServerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_server)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.server_name()
            self.state = 106
            self.match(nginxParser.LBRACE)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611158252812501008) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 511) != 0):
                self.state = 109
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 107
                    self.directive()
                    pass
                elif token in [45, 46, 47, 48, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                    self.state = 108
                    self.parameter()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(nginxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpstreamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def upstream_name(self):
            return self.getTypedRuleContext(nginxParser.Upstream_nameContext,0)


        def upstream_servers(self):
            return self.getTypedRuleContext(nginxParser.Upstream_serversContext,0)


        def LBRACE(self):
            return self.getToken(nginxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nginxParser.RBRACE, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(nginxParser.DirectiveContext,i)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.ParameterContext)
            else:
                return self.getTypedRuleContext(nginxParser.ParameterContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_upstream

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpstream" ):
                listener.enterUpstream(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpstream" ):
                listener.exitUpstream(self)




    def upstream(self):

        localctx = nginxParser.UpstreamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_upstream)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.upstream_name()
            self.state = 117
            self.upstream_servers()
            self.state = 118
            self.match(nginxParser.LBRACE)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611158252812501008) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 511) != 0):
                self.state = 121
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 119
                    self.directive()
                    pass
                elif token in [45, 46, 47, 48, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                    self.state = 120
                    self.parameter()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(nginxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def location_name(self):
            return self.getTypedRuleContext(nginxParser.Location_nameContext,0)


        def LBRACE(self):
            return self.getToken(nginxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nginxParser.RBRACE, 0)

        def location_match(self):
            return self.getTypedRuleContext(nginxParser.Location_matchContext,0)


        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(nginxParser.DirectiveContext,i)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.ParameterContext)
            else:
                return self.getTypedRuleContext(nginxParser.ParameterContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation" ):
                listener.enterLocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation" ):
                listener.exitLocation(self)




    def location(self):

        localctx = nginxParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_location)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.location_name()
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 129
                self.location_match()


            self.state = 132
            self.match(nginxParser.LBRACE)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611158252812501008) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 511) != 0):
                self.state = 135
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 133
                    self.directive()
                    pass
                elif token in [45, 46, 47, 48, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                    self.state = 134
                    self.parameter()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(nginxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_exceptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def limit_except_name(self):
            return self.getTypedRuleContext(nginxParser.Limit_except_nameContext,0)


        def http_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.Http_methodContext)
            else:
                return self.getTypedRuleContext(nginxParser.Http_methodContext,i)


        def LBRACE(self):
            return self.getToken(nginxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nginxParser.RBRACE, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(nginxParser.DirectiveContext,i)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.ParameterContext)
            else:
                return self.getTypedRuleContext(nginxParser.ParameterContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_limit_except

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit_except" ):
                listener.enterLimit_except(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit_except" ):
                listener.exitLimit_except(self)




    def limit_except(self):

        localctx = nginxParser.Limit_exceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_limit_except)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.limit_except_name()
            self.state = 143
            self.http_method()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198889037824) != 0):
                self.state = 144
                self.http_method()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(nginxParser.LBRACE)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611158252812501008) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 511) != 0):
                self.state = 153
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 151
                    self.directive()
                    pass
                elif token in [45, 46, 47, 48, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                    self.state = 152
                    self.parameter()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(nginxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_name(self):
            return self.getTypedRuleContext(nginxParser.If_nameContext,0)


        def if_cond(self):
            return self.getTypedRuleContext(nginxParser.If_condContext,0)


        def LBRACE(self):
            return self.getToken(nginxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nginxParser.RBRACE, 0)

        def directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.DirectiveContext)
            else:
                return self.getTypedRuleContext(nginxParser.DirectiveContext,i)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.ParameterContext)
            else:
                return self.getTypedRuleContext(nginxParser.ParameterContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = nginxParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.if_name()
            self.state = 161
            self.if_cond()
            self.state = 162
            self.match(nginxParser.LBRACE)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611158252812501008) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 511) != 0):
                self.state = 165
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
                    self.state = 163
                    self.directive()
                    pass
                elif token in [45, 46, 47, 48, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                    self.state = 164
                    self.parameter()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(nginxParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include_name(self):
            return self.getTypedRuleContext(nginxParser.Include_nameContext,0)


        def path(self):
            return self.getTypedRuleContext(nginxParser.PathContext,0)


        def SEMI(self):
            return self.getToken(nginxParser.SEMI, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_include

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude" ):
                listener.enterInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude" ):
                listener.exitInclude(self)




    def include(self):

        localctx = nginxParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.include_name()
            self.state = 173
            self.path()
            self.state = 174
            self.match(nginxParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lua_codeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lua_code_name(self):
            return self.getTypedRuleContext(nginxParser.Lua_code_nameContext,0)


        def SEMI(self):
            return self.getToken(nginxParser.SEMI, 0)

        def LUA_CODE(self):
            return self.getToken(nginxParser.LUA_CODE, 0)

        def parameter(self):
            return self.getTypedRuleContext(nginxParser.ParameterContext,0)


        def getRuleIndex(self):
            return nginxParser.RULE_lua_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLua_code" ):
                listener.enterLua_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLua_code" ):
                listener.exitLua_code(self)




    def lua_code(self):

        localctx = nginxParser.Lua_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lua_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.lua_code_name()
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 177
                self.match(nginxParser.LUA_CODE)
                pass
            elif token in [45, 46, 47, 48, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                self.state = 178
                self.parameter()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 181
            self.match(nginxParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(nginxParser.NameContext,0)


        def SEMI(self):
            return self.getToken(nginxParser.SEMI, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.ValueContext)
            else:
                return self.getTypedRuleContext(nginxParser.ValueContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = nginxParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.name()
            self.state = 185 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 184
                self.value()
                self.state = 187 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 41)) & ~0x3f) == 0 and ((1 << (_la - 41)) & 4292870387) != 0)):
                    break

            self.state = 189
            self.match(nginxParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Http_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(nginxParser.GET, 0)

        def HEAD(self):
            return self.getToken(nginxParser.HEAD, 0)

        def POST(self):
            return self.getToken(nginxParser.POST, 0)

        def PUT(self):
            return self.getToken(nginxParser.PUT, 0)

        def DELETE(self):
            return self.getToken(nginxParser.DELETE, 0)

        def MKCOL(self):
            return self.getToken(nginxParser.MKCOL, 0)

        def COPY(self):
            return self.getToken(nginxParser.COPY, 0)

        def MOVE(self):
            return self.getToken(nginxParser.MOVE, 0)

        def OPTIONS(self):
            return self.getToken(nginxParser.OPTIONS, 0)

        def PROPFIND(self):
            return self.getToken(nginxParser.PROPFIND, 0)

        def PROPPATCH(self):
            return self.getToken(nginxParser.PROPPATCH, 0)

        def LOCK(self):
            return self.getToken(nginxParser.LOCK, 0)

        def UNLOCK(self):
            return self.getToken(nginxParser.UNLOCK, 0)

        def PATCH(self):
            return self.getToken(nginxParser.PATCH, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_http_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHttp_method" ):
                listener.enterHttp_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHttp_method" ):
                listener.exitHttp_method(self)




    def http_method(self):

        localctx = nginxParser.Http_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_http_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2198889037824) != 0)):
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


    class If_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(nginxParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(nginxParser.RPAREN, 0)

        def if_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.If_bodyContext)
            else:
                return self.getTypedRuleContext(nginxParser.If_bodyContext,i)


        def getRuleIndex(self):
            return nginxParser.RULE_if_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_cond" ):
                listener.enterIf_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_cond" ):
                listener.exitIf_cond(self)




    def if_cond(self):

        localctx = nginxParser.If_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(nginxParser.LPAREN)
            self.state = 195 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 194
                self.if_body()
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 43)) & ~0x3f) == 0 and ((1 << (_la - 43)) & 1073221631) != 0)):
                    break

            self.state = 199
            self.match(nginxParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_param(self):
            return self.getTypedRuleContext(nginxParser.If_paramContext,0)


        def if_compare(self):
            return self.getTypedRuleContext(nginxParser.If_compareContext,0)


        def if_regexp(self):
            return self.getTypedRuleContext(nginxParser.If_regexpContext,0)


        def if_function(self):
            return self.getTypedRuleContext(nginxParser.If_functionContext,0)


        def if_str(self):
            return self.getTypedRuleContext(nginxParser.If_strContext,0)


        def getRuleIndex(self):
            return nginxParser.RULE_if_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_body" ):
                listener.enterIf_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_body" ):
                listener.exitIf_body(self)




    def if_body(self):

        localctx = nginxParser.If_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 201
                self.if_param()
                pass

            elif la_ == 2:
                self.state = 202
                self.if_compare()
                pass

            elif la_ == 3:
                self.state = 203
                self.if_regexp()
                pass

            elif la_ == 4:
                self.state = 204
                self.if_function()
                pass

            elif la_ == 5:
                self.state = 205
                self.if_str()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(nginxParser.DOLLAR, 0)

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.NameContext)
            else:
                return self.getTypedRuleContext(nginxParser.NameContext,i)


        def LBRACE(self):
            return self.getToken(nginxParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nginxParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.COMMA)
            else:
                return self.getToken(nginxParser.COMMA, i)

        def getRuleIndex(self):
            return nginxParser.RULE_if_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_param" ):
                listener.enterIf_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_param" ):
                listener.exitIf_param(self)




    def if_param(self):

        localctx = nginxParser.If_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 208
                self.match(nginxParser.DOLLAR)
                self.state = 209
                self.name()
                pass

            elif la_ == 2:
                self.state = 210
                self.match(nginxParser.DOLLAR)
                self.state = 211
                self.name()
                self.state = 212
                self.match(nginxParser.LBRACE)
                self.state = 213
                self.name()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 214
                    self.match(nginxParser.COMMA)
                    self.state = 215
                    self.name()
                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 221
                self.match(nginxParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_compareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(nginxParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(nginxParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_if_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_compare" ):
                listener.enterIf_compare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_compare" ):
                listener.exitIf_compare(self)




    def if_compare(self):

        localctx = nginxParser.If_compareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
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


    class If_regexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGEXP_START(self):
            return self.getToken(nginxParser.REGEXP_START, 0)

        def REGEXP_START_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_NOT, 0)

        def REGEXP_START_CASE(self):
            return self.getToken(nginxParser.REGEXP_START_CASE, 0)

        def REGEXP_START_CASE_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_CASE_NOT, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_if_regexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_regexp" ):
                listener.enterIf_regexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_regexp" ):
                listener.exitIf_regexp(self)




    def if_regexp(self):

        localctx = nginxParser.If_regexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_regexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 527765581332480) != 0)):
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


    class If_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILE_EXIST(self):
            return self.getToken(nginxParser.FILE_EXIST, 0)

        def FILE_NOT_EXIST(self):
            return self.getToken(nginxParser.FILE_NOT_EXIST, 0)

        def FILE_DIR_EXIST(self):
            return self.getToken(nginxParser.FILE_DIR_EXIST, 0)

        def FILE_DIR_NOT_EXIST(self):
            return self.getToken(nginxParser.FILE_DIR_NOT_EXIST, 0)

        def FILE_EXE_EXIST(self):
            return self.getToken(nginxParser.FILE_EXE_EXIST, 0)

        def FILE_EXE_NOT_EXIST(self):
            return self.getToken(nginxParser.FILE_EXE_NOT_EXIST, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_if_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_function" ):
                listener.enterIf_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_function" ):
                listener.exitIf_function(self)




    def if_function(self):

        localctx = nginxParser.If_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35465847065542656) != 0)):
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


    class If_strContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(nginxParser.WORD, 0)

        def SINGLE_STRING(self):
            return self.getToken(nginxParser.SINGLE_STRING, 0)

        def DOUBLE_STRING(self):
            return self.getToken(nginxParser.DOUBLE_STRING, 0)

        def path(self):
            return self.getTypedRuleContext(nginxParser.PathContext,0)


        def DOLLAR(self):
            return self.getToken(nginxParser.DOLLAR, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_if_str

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_str" ):
                listener.enterIf_str(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_str" ):
                listener.exitIf_str(self)




    def if_str(self):

        localctx = nginxParser.If_strContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 231
                self.match(nginxParser.WORD)
                pass

            elif la_ == 2:
                self.state = 232
                self.match(nginxParser.SINGLE_STRING)
                pass

            elif la_ == 3:
                self.state = 233
                self.match(nginxParser.DOUBLE_STRING)
                pass

            elif la_ == 4:
                self.state = 234
                self.path()
                pass

            elif la_ == 5:
                self.state = 235
                self.match(nginxParser.DOLLAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Upstream_serversContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(nginxParser.DOLLAR, 0)

        def name(self):
            return self.getTypedRuleContext(nginxParser.NameContext,0)


        def getRuleIndex(self):
            return nginxParser.RULE_upstream_servers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpstream_servers" ):
                listener.enterUpstream_servers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpstream_servers" ):
                listener.exitUpstream_servers(self)




    def upstream_servers(self):

        localctx = nginxParser.Upstream_serversContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_upstream_servers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 238
                self.match(nginxParser.DOLLAR)
                self.state = 239
                self.name()
                pass

            elif la_ == 2:
                self.state = 240
                self.name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Location_matchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(nginxParser.EQUAL, 0)

        def REGEXP_START(self):
            return self.getToken(nginxParser.REGEXP_START, 0)

        def REGEXP_START_CASE(self):
            return self.getToken(nginxParser.REGEXP_START_CASE, 0)

        def REGEXP_START_CASE_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_CASE_NOT, 0)

        def REGEXP_START_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_NOT, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_location_match

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation_match" ):
                listener.enterLocation_match(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation_match" ):
                listener.exitLocation_match(self)




    def location_match(self):

        localctx = nginxParser.Location_matchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_location_match)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 536561674354688) != 0):
                self.state = 243
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 536561674354688) != 0)):
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


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(nginxParser.WORD, 0)

        def SINGLE_STRING(self):
            return self.getToken(nginxParser.SINGLE_STRING, 0)

        def DOUBLE_STRING(self):
            return self.getToken(nginxParser.DOUBLE_STRING, 0)

        def path(self):
            return self.getTypedRuleContext(nginxParser.PathContext,0)


        def REGEXP_START(self):
            return self.getToken(nginxParser.REGEXP_START, 0)

        def REGEXP_START_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_NOT, 0)

        def REGEXP_START_CASE(self):
            return self.getToken(nginxParser.REGEXP_START_CASE, 0)

        def REGEXP_START_CASE_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_CASE_NOT, 0)

        def DOLLAR(self):
            return self.getToken(nginxParser.DOLLAR, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = nginxParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 246
                self.match(nginxParser.WORD)
                pass

            elif la_ == 2:
                self.state = 247
                self.match(nginxParser.SINGLE_STRING)
                pass

            elif la_ == 3:
                self.state = 248
                self.match(nginxParser.DOUBLE_STRING)
                pass

            elif la_ == 4:
                self.state = 249
                self.path()
                pass

            elif la_ == 5:
                self.state = 250
                self.match(nginxParser.REGEXP_START)
                pass

            elif la_ == 6:
                self.state = 251
                self.match(nginxParser.REGEXP_START_NOT)
                pass

            elif la_ == 7:
                self.state = 252
                self.match(nginxParser.REGEXP_START_CASE)
                pass

            elif la_ == 8:
                self.state = 253
                self.match(nginxParser.REGEXP_START_CASE_NOT)
                pass

            elif la_ == 9:
                self.state = 254
                self.match(nginxParser.DOLLAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(nginxParser.WORD, 0)

        def SINGLE_STRING(self):
            return self.getToken(nginxParser.SINGLE_STRING, 0)

        def DOUBLE_STRING(self):
            return self.getToken(nginxParser.DOUBLE_STRING, 0)

        def path(self):
            return self.getTypedRuleContext(nginxParser.PathContext,0)


        def REGEXP_START(self):
            return self.getToken(nginxParser.REGEXP_START, 0)

        def REGEXP_START_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_NOT, 0)

        def REGEXP_START_CASE(self):
            return self.getToken(nginxParser.REGEXP_START_CASE, 0)

        def REGEXP_START_CASE_NOT(self):
            return self.getToken(nginxParser.REGEXP_START_CASE_NOT, 0)

        def DOLLAR(self):
            return self.getToken(nginxParser.DOLLAR, 0)

        def on(self):
            return self.getTypedRuleContext(nginxParser.OnContext,0)


        def off(self):
            return self.getTypedRuleContext(nginxParser.OffContext,0)


        def getRuleIndex(self):
            return nginxParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = nginxParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 257
                self.match(nginxParser.WORD)
                pass

            elif la_ == 2:
                self.state = 258
                self.match(nginxParser.SINGLE_STRING)
                pass

            elif la_ == 3:
                self.state = 259
                self.match(nginxParser.DOUBLE_STRING)
                pass

            elif la_ == 4:
                self.state = 260
                self.path()
                pass

            elif la_ == 5:
                self.state = 261
                self.match(nginxParser.REGEXP_START)
                pass

            elif la_ == 6:
                self.state = 262
                self.match(nginxParser.REGEXP_START_NOT)
                pass

            elif la_ == 7:
                self.state = 263
                self.match(nginxParser.REGEXP_START_CASE)
                pass

            elif la_ == 8:
                self.state = 264
                self.match(nginxParser.REGEXP_START_CASE_NOT)
                pass

            elif la_ == 9:
                self.state = 265
                self.match(nginxParser.DOLLAR)
                pass

            elif la_ == 10:
                self.state = 266
                self.on()
                pass

            elif la_ == 11:
                self.state = 267
                self.off()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(nginxParser.ON, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_on

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn" ):
                listener.enterOn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn" ):
                listener.exitOn(self)




    def on(self):

        localctx = nginxParser.OnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_on)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(nginxParser.ON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OFF(self):
            return self.getToken(nginxParser.OFF, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_off

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOff" ):
                listener.enterOff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOff" ):
                listener.exitOff(self)




    def off(self):

        localctx = nginxParser.OffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_off)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(nginxParser.OFF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RSLASH(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.RSLASH)
            else:
                return self.getToken(nginxParser.RSLASH, i)

        def path_component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nginxParser.Path_componentContext)
            else:
                return self.getTypedRuleContext(nginxParser.Path_componentContext,i)


        def POINT(self):
            return self.getToken(nginxParser.POINT, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)




    def path(self):

        localctx = nginxParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 274
                self.match(nginxParser.RSLASH)

            elif la_ == 2:
                self.state = 275
                self.match(nginxParser.RSLASH)
                self.state = 276
                self.match(nginxParser.RSLASH)


            self.state = 280 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 279
                    self.path_component()

                else:
                    raise NoViableAltException(self)
                self.state = 282 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 284
                self.match(nginxParser.RSLASH)

            elif la_ == 2:
                self.state = 285
                self.match(nginxParser.RSLASH)
                self.state = 286
                self.match(nginxParser.RSLASH)

            elif la_ == 3:
                self.state = 287
                self.match(nginxParser.POINT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Path_componentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.WORD)
            else:
                return self.getToken(nginxParser.WORD, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.INTEGER)
            else:
                return self.getToken(nginxParser.INTEGER, i)

        def DOLLAR(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.DOLLAR)
            else:
                return self.getToken(nginxParser.DOLLAR, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.MINUS)
            else:
                return self.getToken(nginxParser.MINUS, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.UNDERSCORE)
            else:
                return self.getToken(nginxParser.UNDERSCORE, i)

        def TILDE(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.TILDE)
            else:
                return self.getToken(nginxParser.TILDE, i)

        def POINT(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.POINT)
            else:
                return self.getToken(nginxParser.POINT, i)

        def ASTERISK(self, i:int=None):
            if i is None:
                return self.getTokens(nginxParser.ASTERISK)
            else:
                return self.getToken(nginxParser.ASTERISK, i)

        def getRuleIndex(self):
            return nginxParser.RULE_path_component

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath_component" ):
                listener.enterPath_component(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath_component" ):
                listener.exitPath_component(self)




    def path_component(self):

        localctx = nginxParser.Path_componentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_path_component)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 290
                    _la = self._input.LA(1)
                    if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 255) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 293 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Http_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HTTP(self):
            return self.getToken(nginxParser.HTTP, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_http_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHttp_name" ):
                listener.enterHttp_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHttp_name" ):
                listener.exitHttp_name(self)




    def http_name(self):

        localctx = nginxParser.Http_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_http_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(nginxParser.HTTP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Server_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERVER(self):
            return self.getToken(nginxParser.SERVER, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_server_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServer_name" ):
                listener.enterServer_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServer_name" ):
                listener.exitServer_name(self)




    def server_name(self):

        localctx = nginxParser.Server_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_server_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(nginxParser.SERVER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Upstream_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPSTREAM(self):
            return self.getToken(nginxParser.UPSTREAM, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_upstream_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpstream_name" ):
                listener.enterUpstream_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpstream_name" ):
                listener.exitUpstream_name(self)




    def upstream_name(self):

        localctx = nginxParser.Upstream_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_upstream_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(nginxParser.UPSTREAM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Location_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCATION(self):
            return self.getToken(nginxParser.LOCATION, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_location_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation_name" ):
                listener.enterLocation_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation_name" ):
                listener.exitLocation_name(self)




    def location_name(self):

        localctx = nginxParser.Location_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_location_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(nginxParser.LOCATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(nginxParser.IF, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_if_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_name" ):
                listener.enterIf_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_name" ):
                listener.exitIf_name(self)




    def if_name(self):

        localctx = nginxParser.If_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(nginxParser.IF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(nginxParser.INCLUDE, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_include_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude_name" ):
                listener.enterInclude_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude_name" ):
                listener.exitInclude_name(self)




    def include_name(self):

        localctx = nginxParser.Include_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_include_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(nginxParser.INCLUDE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_except_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMIT_EXCEPT(self):
            return self.getToken(nginxParser.LIMIT_EXCEPT, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_limit_except_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit_except_name" ):
                listener.enterLimit_except_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit_except_name" ):
                listener.exitLimit_except_name(self)




    def limit_except_name(self):

        localctx = nginxParser.Limit_except_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_limit_except_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(nginxParser.LIMIT_EXCEPT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lua_code_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LUA_BY_REWRITE(self):
            return self.getToken(nginxParser.LUA_BY_REWRITE, 0)

        def LUA_BY_ACCESS(self):
            return self.getToken(nginxParser.LUA_BY_ACCESS, 0)

        def LUA_BY_CONTENT(self):
            return self.getToken(nginxParser.LUA_BY_CONTENT, 0)

        def LUA_BY_HEADER_FILTER(self):
            return self.getToken(nginxParser.LUA_BY_HEADER_FILTER, 0)

        def LUA_BY_BODY_FILTER(self):
            return self.getToken(nginxParser.LUA_BY_BODY_FILTER, 0)

        def LUA_BY_LOG(self):
            return self.getToken(nginxParser.LUA_BY_LOG, 0)

        def LUA_BY_BALANCER(self):
            return self.getToken(nginxParser.LUA_BY_BALANCER, 0)

        def LUA_BY_INIT(self):
            return self.getToken(nginxParser.LUA_BY_INIT, 0)

        def LUA_BY_INIT_WORKER(self):
            return self.getToken(nginxParser.LUA_BY_INIT_WORKER, 0)

        def LUA_BY_EXIT_WORKER(self):
            return self.getToken(nginxParser.LUA_BY_EXIT_WORKER, 0)

        def LUA_BY_EXIT_MASTER(self):
            return self.getToken(nginxParser.LUA_BY_EXIT_MASTER, 0)

        def LUA_BY_SSL_CERT(self):
            return self.getToken(nginxParser.LUA_BY_SSL_CERT, 0)

        def LUA_BY_SSL_CLIENT_HELLO(self):
            return self.getToken(nginxParser.LUA_BY_SSL_CLIENT_HELLO, 0)

        def LUA_BY_SHARED_DICT(self):
            return self.getToken(nginxParser.LUA_BY_SHARED_DICT, 0)

        def getRuleIndex(self):
            return nginxParser.RULE_lua_code_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLua_code_name" ):
                listener.enterLua_code_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLua_code_name" ):
                listener.exitLua_code_name(self)




    def lua_code_name(self):

        localctx = nginxParser.Lua_code_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_lua_code_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33552384) != 0)):
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





