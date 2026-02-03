# Generated from ./backend/grammar/dk.g4 by ANTLR 4.13.1
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
        4,1,53,314,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,5,0,74,8,0,10,0,12,0,77,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,99,8,1,1,1,1,1,1,1,1,1,1,1,3,1,106,8,1,1,2,1,2,3,2,110,
        8,2,1,2,1,2,3,2,114,8,2,1,2,3,2,117,8,2,1,3,1,3,1,3,3,3,122,8,3,
        1,4,1,4,1,4,3,4,127,8,4,1,5,1,5,1,5,5,5,132,8,5,10,5,12,5,135,9,
        5,1,6,1,6,4,6,139,8,6,11,6,12,6,140,1,7,1,7,1,7,5,7,146,8,7,10,7,
        12,7,149,9,7,1,8,1,8,1,8,3,8,154,8,8,1,9,1,9,5,9,158,8,9,10,9,12,
        9,161,9,9,1,9,1,9,1,9,1,10,1,10,5,10,168,8,10,10,10,12,10,171,9,
        10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,179,8,11,1,12,1,12,1,12,3,
        12,184,8,12,1,13,1,13,1,13,1,13,1,13,3,13,191,8,13,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,3,15,201,8,15,1,16,1,16,1,16,1,17,1,17,
        1,17,1,18,1,18,1,18,3,18,212,8,18,1,19,1,19,1,19,1,20,1,20,1,20,
        1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        3,23,233,8,23,1,24,1,24,1,24,3,24,238,8,24,1,24,1,24,1,24,1,24,3,
        24,244,8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,
        27,1,28,4,28,258,8,28,11,28,12,28,259,1,29,1,29,5,29,264,8,29,10,
        29,12,29,267,9,29,1,30,1,30,1,30,1,30,5,30,273,8,30,10,30,12,30,
        276,9,30,1,30,1,30,1,31,1,31,1,31,1,31,5,31,284,8,31,10,31,12,31,
        287,9,31,1,31,1,31,1,32,4,32,292,8,32,11,32,12,32,293,1,33,1,33,
        1,34,5,34,299,8,34,10,34,12,34,302,9,34,1,34,1,34,1,34,3,34,307,
        8,34,1,35,1,35,1,35,1,35,1,35,1,35,0,0,36,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,0,5,2,0,36,36,38,38,2,0,6,6,27,28,3,0,36,36,38,38,
        44,50,1,0,30,33,1,0,3,5,323,0,75,1,0,0,0,2,105,1,0,0,0,4,107,1,0,
        0,0,6,118,1,0,0,0,8,123,1,0,0,0,10,128,1,0,0,0,12,136,1,0,0,0,14,
        142,1,0,0,0,16,150,1,0,0,0,18,155,1,0,0,0,20,165,1,0,0,0,22,175,
        1,0,0,0,24,180,1,0,0,0,26,185,1,0,0,0,28,192,1,0,0,0,30,195,1,0,
        0,0,32,202,1,0,0,0,34,205,1,0,0,0,36,208,1,0,0,0,38,213,1,0,0,0,
        40,216,1,0,0,0,42,219,1,0,0,0,44,222,1,0,0,0,46,226,1,0,0,0,48,234,
        1,0,0,0,50,245,1,0,0,0,52,249,1,0,0,0,54,253,1,0,0,0,56,257,1,0,
        0,0,58,261,1,0,0,0,60,268,1,0,0,0,62,279,1,0,0,0,64,291,1,0,0,0,
        66,295,1,0,0,0,68,300,1,0,0,0,70,308,1,0,0,0,72,74,3,2,1,0,73,72,
        1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,
        77,75,1,0,0,0,78,79,5,0,0,1,79,1,1,0,0,0,80,99,3,4,2,0,81,99,3,6,
        3,0,82,99,3,8,4,0,83,99,3,10,5,0,84,99,3,12,6,0,85,99,3,14,7,0,86,
        99,3,16,8,0,87,99,3,18,9,0,88,99,3,20,10,0,89,99,3,22,11,0,90,99,
        3,24,12,0,91,99,3,26,13,0,92,99,3,28,14,0,93,99,3,30,15,0,94,99,
        3,32,16,0,95,99,3,34,17,0,96,99,3,36,18,0,97,99,3,38,19,0,98,80,
        1,0,0,0,98,81,1,0,0,0,98,82,1,0,0,0,98,83,1,0,0,0,98,84,1,0,0,0,
        98,85,1,0,0,0,98,86,1,0,0,0,98,87,1,0,0,0,98,88,1,0,0,0,98,89,1,
        0,0,0,98,90,1,0,0,0,98,91,1,0,0,0,98,92,1,0,0,0,98,93,1,0,0,0,98,
        94,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,100,1,0,
        0,0,100,101,5,35,0,0,101,106,1,0,0,0,102,103,5,34,0,0,103,106,5,
        35,0,0,104,106,5,35,0,0,105,98,1,0,0,0,105,102,1,0,0,0,105,104,1,
        0,0,0,106,3,1,0,0,0,107,109,5,6,0,0,108,110,3,40,20,0,109,108,1,
        0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,113,3,48,24,0,112,114,
        3,42,21,0,113,112,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,117,
        3,44,22,0,116,115,1,0,0,0,116,117,1,0,0,0,117,5,1,0,0,0,118,121,
        5,7,0,0,119,122,3,60,30,0,120,122,3,64,32,0,121,119,1,0,0,0,121,
        120,1,0,0,0,122,7,1,0,0,0,123,126,5,8,0,0,124,127,3,60,30,0,125,
        127,3,64,32,0,126,124,1,0,0,0,126,125,1,0,0,0,127,9,1,0,0,0,128,
        129,5,9,0,0,129,133,3,50,25,0,130,132,3,50,25,0,131,130,1,0,0,0,
        132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,11,1,0,0,0,135,
        133,1,0,0,0,136,138,5,10,0,0,137,139,5,51,0,0,138,137,1,0,0,0,139,
        140,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,13,1,0,0,0,142,143,
        5,11,0,0,143,147,5,36,0,0,144,146,5,36,0,0,145,144,1,0,0,0,146,149,
        1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,15,1,0,0,0,149,147,1,
        0,0,0,150,153,5,12,0,0,151,154,3,52,26,0,152,154,3,54,27,0,153,151,
        1,0,0,0,153,152,1,0,0,0,154,17,1,0,0,0,155,159,5,13,0,0,156,158,
        3,46,23,0,157,156,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,
        1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,3,56,28,0,163,164,
        3,56,28,0,164,19,1,0,0,0,165,169,5,14,0,0,166,168,3,46,23,0,167,
        166,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,
        172,1,0,0,0,171,169,1,0,0,0,172,173,3,56,28,0,173,174,3,56,28,0,
        174,21,1,0,0,0,175,178,5,15,0,0,176,179,3,60,30,0,177,179,3,64,32,
        0,178,176,1,0,0,0,178,177,1,0,0,0,179,23,1,0,0,0,180,183,5,16,0,
        0,181,184,3,62,31,0,182,184,3,58,29,0,183,181,1,0,0,0,183,182,1,
        0,0,0,184,25,1,0,0,0,185,190,5,17,0,0,186,191,5,36,0,0,187,188,5,
        36,0,0,188,189,5,1,0,0,189,191,5,36,0,0,190,186,1,0,0,0,190,187,
        1,0,0,0,191,27,1,0,0,0,192,193,5,18,0,0,193,194,3,56,28,0,194,29,
        1,0,0,0,195,200,5,19,0,0,196,201,5,36,0,0,197,198,5,36,0,0,198,199,
        5,41,0,0,199,201,7,0,0,0,200,196,1,0,0,0,200,197,1,0,0,0,201,31,
        1,0,0,0,202,203,5,20,0,0,203,204,3,2,1,0,204,33,1,0,0,0,205,206,
        5,21,0,0,206,207,5,36,0,0,207,35,1,0,0,0,208,211,5,22,0,0,209,212,
        3,66,33,0,210,212,3,68,34,0,211,209,1,0,0,0,211,210,1,0,0,0,212,
        37,1,0,0,0,213,214,5,23,0,0,214,215,3,62,31,0,215,39,1,0,0,0,216,
        217,5,29,0,0,217,218,5,36,0,0,218,41,1,0,0,0,219,220,5,25,0,0,220,
        221,5,36,0,0,221,43,1,0,0,0,222,223,5,26,0,0,223,224,5,41,0,0,224,
        225,5,36,0,0,225,45,1,0,0,0,226,227,7,1,0,0,227,232,5,41,0,0,228,
        233,5,36,0,0,229,230,5,36,0,0,230,231,5,1,0,0,231,233,5,36,0,0,232,
        228,1,0,0,0,232,229,1,0,0,0,233,47,1,0,0,0,234,237,5,36,0,0,235,
        236,5,1,0,0,236,238,5,36,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,
        243,1,0,0,0,239,240,5,2,0,0,240,241,5,36,0,0,241,242,5,1,0,0,242,
        244,5,36,0,0,243,239,1,0,0,0,243,244,1,0,0,0,244,49,1,0,0,0,245,
        246,5,36,0,0,246,247,5,41,0,0,247,248,7,0,0,0,248,51,1,0,0,0,249,
        250,5,36,0,0,250,251,5,41,0,0,251,252,7,0,0,0,252,53,1,0,0,0,253,
        254,5,36,0,0,254,255,7,0,0,0,255,55,1,0,0,0,256,258,7,2,0,0,257,
        256,1,0,0,0,258,259,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,
        57,1,0,0,0,261,265,3,56,28,0,262,264,3,56,28,0,263,262,1,0,0,0,264,
        267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,59,1,0,0,0,267,265,
        1,0,0,0,268,269,5,39,0,0,269,274,5,38,0,0,270,271,5,42,0,0,271,273,
        5,38,0,0,272,270,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,
        1,0,0,0,275,277,1,0,0,0,276,274,1,0,0,0,277,278,5,40,0,0,278,61,
        1,0,0,0,279,280,5,39,0,0,280,285,5,38,0,0,281,282,5,42,0,0,282,284,
        5,38,0,0,283,281,1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,285,286,
        1,0,0,0,286,288,1,0,0,0,287,285,1,0,0,0,288,289,5,40,0,0,289,63,
        1,0,0,0,290,292,5,51,0,0,291,290,1,0,0,0,292,293,1,0,0,0,293,291,
        1,0,0,0,293,294,1,0,0,0,294,65,1,0,0,0,295,296,5,24,0,0,296,67,1,
        0,0,0,297,299,3,70,35,0,298,297,1,0,0,0,299,302,1,0,0,0,300,298,
        1,0,0,0,300,301,1,0,0,0,301,303,1,0,0,0,302,300,1,0,0,0,303,306,
        5,8,0,0,304,307,3,60,30,0,305,307,3,64,32,0,306,304,1,0,0,0,306,
        305,1,0,0,0,307,69,1,0,0,0,308,309,7,3,0,0,309,310,5,41,0,0,310,
        311,5,37,0,0,311,312,7,4,0,0,312,71,1,0,0,0,29,75,98,105,109,113,
        116,121,126,133,140,147,153,159,169,178,183,190,200,211,232,237,
        243,259,265,274,285,293,300,306
    ]

class dkParser ( Parser ):

    grammarFileName = "dk.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'@'", "'s'", "'ms'", "'m'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'--chown'", "'--chmod'", "'--platform'", "'--interval'", 
                     "'--timeout'", "'--start-period'", "'--retries'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "'='", "','", "'#'", "'/'", "'*'", "'$'", 
                     "'.'", "'-'", "'_'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FROM", "RUN", "CMD", "LABEL", 
                      "MAINTAINER", "EXPOSE", "ENV", "ADD", "COPY", "ENTRYPOINT", 
                      "VOLUME", "USER", "WORKDIR", "ARG", "ONBUILD", "STOPSIGNAL", 
                      "HEALTHCHECK", "SHELL", "NONE", "AS", "NAME", "CHOWN", 
                      "CHMOD", "PLATFORM", "INTERVAL", "TIMEOUT", "START_PERIOD", 
                      "RETRIES", "COMMENT", "NEWLINE", "WORD", "INTEGER", 
                      "QUOTED_STRING", "LBRACKET", "RBRACKET", "EQ", "COMMA", 
                      "HASH", "RSLASH", "ASTERISK", "DOLLAR", "POINT", "MINUS", 
                      "UNDERSCORE", "TILDE", "ANY_CHAR_EXCEPT_NEWLINE", 
                      "WS", "LINE_CONTINUATION" ]

    RULE_dockerfile = 0
    RULE_instruction = 1
    RULE_from = 2
    RULE_run = 3
    RULE_cmd = 4
    RULE_label = 5
    RULE_maintainer = 6
    RULE_expose = 7
    RULE_env = 8
    RULE_add = 9
    RULE_copy = 10
    RULE_entrypoint = 11
    RULE_volume = 12
    RULE_user = 13
    RULE_workdir = 14
    RULE_arg = 15
    RULE_onbuild = 16
    RULE_stopsignal = 17
    RULE_healthcheck = 18
    RULE_shell = 19
    RULE_platform_opt = 20
    RULE_as_opt = 21
    RULE_name_opt = 22
    RULE_param_opt = 23
    RULE_image_spec = 24
    RULE_label_pair = 25
    RULE_env_pair = 26
    RULE_env_single = 27
    RULE_path_spec = 28
    RULE_shell_command_paths = 29
    RULE_json_command = 30
    RULE_json_array = 31
    RULE_shell_command = 32
    RULE_health_none = 33
    RULE_health_cmd = 34
    RULE_options_opt = 35

    ruleNames =  [ "dockerfile", "instruction", "from", "run", "cmd", "label", 
                   "maintainer", "expose", "env", "add", "copy", "entrypoint", 
                   "volume", "user", "workdir", "arg", "onbuild", "stopsignal", 
                   "healthcheck", "shell", "platform_opt", "as_opt", "name_opt", 
                   "param_opt", "image_spec", "label_pair", "env_pair", 
                   "env_single", "path_spec", "shell_command_paths", "json_command", 
                   "json_array", "shell_command", "health_none", "health_cmd", 
                   "options_opt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    FROM=6
    RUN=7
    CMD=8
    LABEL=9
    MAINTAINER=10
    EXPOSE=11
    ENV=12
    ADD=13
    COPY=14
    ENTRYPOINT=15
    VOLUME=16
    USER=17
    WORKDIR=18
    ARG=19
    ONBUILD=20
    STOPSIGNAL=21
    HEALTHCHECK=22
    SHELL=23
    NONE=24
    AS=25
    NAME=26
    CHOWN=27
    CHMOD=28
    PLATFORM=29
    INTERVAL=30
    TIMEOUT=31
    START_PERIOD=32
    RETRIES=33
    COMMENT=34
    NEWLINE=35
    WORD=36
    INTEGER=37
    QUOTED_STRING=38
    LBRACKET=39
    RBRACKET=40
    EQ=41
    COMMA=42
    HASH=43
    RSLASH=44
    ASTERISK=45
    DOLLAR=46
    POINT=47
    MINUS=48
    UNDERSCORE=49
    TILDE=50
    ANY_CHAR_EXCEPT_NEWLINE=51
    WS=52
    LINE_CONTINUATION=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DockerfileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(dkParser.EOF, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.InstructionContext)
            else:
                return self.getTypedRuleContext(dkParser.InstructionContext,i)


        def getRuleIndex(self):
            return dkParser.RULE_dockerfile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDockerfile" ):
                listener.enterDockerfile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDockerfile" ):
                listener.exitDockerfile(self)




    def dockerfile(self):

        localctx = dkParser.DockerfileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dockerfile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 51556384704) != 0):
                self.state = 72
                self.instruction()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(dkParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(dkParser.NEWLINE, 0)

        def from_(self):
            return self.getTypedRuleContext(dkParser.FromContext,0)


        def run(self):
            return self.getTypedRuleContext(dkParser.RunContext,0)


        def cmd(self):
            return self.getTypedRuleContext(dkParser.CmdContext,0)


        def label(self):
            return self.getTypedRuleContext(dkParser.LabelContext,0)


        def maintainer(self):
            return self.getTypedRuleContext(dkParser.MaintainerContext,0)


        def expose(self):
            return self.getTypedRuleContext(dkParser.ExposeContext,0)


        def env(self):
            return self.getTypedRuleContext(dkParser.EnvContext,0)


        def add(self):
            return self.getTypedRuleContext(dkParser.AddContext,0)


        def copy(self):
            return self.getTypedRuleContext(dkParser.CopyContext,0)


        def entrypoint(self):
            return self.getTypedRuleContext(dkParser.EntrypointContext,0)


        def volume(self):
            return self.getTypedRuleContext(dkParser.VolumeContext,0)


        def user(self):
            return self.getTypedRuleContext(dkParser.UserContext,0)


        def workdir(self):
            return self.getTypedRuleContext(dkParser.WorkdirContext,0)


        def arg(self):
            return self.getTypedRuleContext(dkParser.ArgContext,0)


        def onbuild(self):
            return self.getTypedRuleContext(dkParser.OnbuildContext,0)


        def stopsignal(self):
            return self.getTypedRuleContext(dkParser.StopsignalContext,0)


        def healthcheck(self):
            return self.getTypedRuleContext(dkParser.HealthcheckContext,0)


        def shell(self):
            return self.getTypedRuleContext(dkParser.ShellContext,0)


        def COMMENT(self):
            return self.getToken(dkParser.COMMENT, 0)

        def getRuleIndex(self):
            return dkParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = dkParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 80
                    self.from_()
                    pass
                elif token in [7]:
                    self.state = 81
                    self.run()
                    pass
                elif token in [8]:
                    self.state = 82
                    self.cmd()
                    pass
                elif token in [9]:
                    self.state = 83
                    self.label()
                    pass
                elif token in [10]:
                    self.state = 84
                    self.maintainer()
                    pass
                elif token in [11]:
                    self.state = 85
                    self.expose()
                    pass
                elif token in [12]:
                    self.state = 86
                    self.env()
                    pass
                elif token in [13]:
                    self.state = 87
                    self.add()
                    pass
                elif token in [14]:
                    self.state = 88
                    self.copy()
                    pass
                elif token in [15]:
                    self.state = 89
                    self.entrypoint()
                    pass
                elif token in [16]:
                    self.state = 90
                    self.volume()
                    pass
                elif token in [17]:
                    self.state = 91
                    self.user()
                    pass
                elif token in [18]:
                    self.state = 92
                    self.workdir()
                    pass
                elif token in [19]:
                    self.state = 93
                    self.arg()
                    pass
                elif token in [20]:
                    self.state = 94
                    self.onbuild()
                    pass
                elif token in [21]:
                    self.state = 95
                    self.stopsignal()
                    pass
                elif token in [22]:
                    self.state = 96
                    self.healthcheck()
                    pass
                elif token in [23]:
                    self.state = 97
                    self.shell()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 100
                self.match(dkParser.NEWLINE)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(dkParser.COMMENT)
                self.state = 103
                self.match(dkParser.NEWLINE)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(dkParser.NEWLINE)
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


    class FromContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(dkParser.FROM, 0)

        def image_spec(self):
            return self.getTypedRuleContext(dkParser.Image_specContext,0)


        def platform_opt(self):
            return self.getTypedRuleContext(dkParser.Platform_optContext,0)


        def as_opt(self):
            return self.getTypedRuleContext(dkParser.As_optContext,0)


        def name_opt(self):
            return self.getTypedRuleContext(dkParser.Name_optContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_from

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom" ):
                listener.enterFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom" ):
                listener.exitFrom(self)




    def from_(self):

        localctx = dkParser.FromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_from)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(dkParser.FROM)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 108
                self.platform_opt()


            self.state = 111
            self.image_spec()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 112
                self.as_opt()


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 115
                self.name_opt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RUN(self):
            return self.getToken(dkParser.RUN, 0)

        def json_command(self):
            return self.getTypedRuleContext(dkParser.Json_commandContext,0)


        def shell_command(self):
            return self.getTypedRuleContext(dkParser.Shell_commandContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_run

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRun" ):
                listener.enterRun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRun" ):
                listener.exitRun(self)




    def run(self):

        localctx = dkParser.RunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_run)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(dkParser.RUN)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 119
                self.json_command()
                pass
            elif token in [51]:
                self.state = 120
                self.shell_command()
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


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMD(self):
            return self.getToken(dkParser.CMD, 0)

        def json_command(self):
            return self.getTypedRuleContext(dkParser.Json_commandContext,0)


        def shell_command(self):
            return self.getTypedRuleContext(dkParser.Shell_commandContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = dkParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(dkParser.CMD)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 124
                self.json_command()
                pass
            elif token in [51]:
                self.state = 125
                self.shell_command()
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


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(dkParser.LABEL, 0)

        def label_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.Label_pairContext)
            else:
                return self.getTypedRuleContext(dkParser.Label_pairContext,i)


        def getRuleIndex(self):
            return dkParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = dkParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(dkParser.LABEL)
            self.state = 129
            self.label_pair()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 130
                self.label_pair()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaintainerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAINTAINER(self):
            return self.getToken(dkParser.MAINTAINER, 0)

        def ANY_CHAR_EXCEPT_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.ANY_CHAR_EXCEPT_NEWLINE)
            else:
                return self.getToken(dkParser.ANY_CHAR_EXCEPT_NEWLINE, i)

        def getRuleIndex(self):
            return dkParser.RULE_maintainer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaintainer" ):
                listener.enterMaintainer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaintainer" ):
                listener.exitMaintainer(self)




    def maintainer(self):

        localctx = dkParser.MaintainerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_maintainer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(dkParser.MAINTAINER)
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.match(dkParser.ANY_CHAR_EXCEPT_NEWLINE)
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExposeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPOSE(self):
            return self.getToken(dkParser.EXPOSE, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def getRuleIndex(self):
            return dkParser.RULE_expose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpose" ):
                listener.enterExpose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpose" ):
                listener.exitExpose(self)




    def expose(self):

        localctx = dkParser.ExposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expose)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(dkParser.EXPOSE)
            self.state = 143
            self.match(dkParser.WORD)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 144
                self.match(dkParser.WORD)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENV(self):
            return self.getToken(dkParser.ENV, 0)

        def env_pair(self):
            return self.getTypedRuleContext(dkParser.Env_pairContext,0)


        def env_single(self):
            return self.getTypedRuleContext(dkParser.Env_singleContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_env

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv" ):
                listener.enterEnv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv" ):
                listener.exitEnv(self)




    def env(self):

        localctx = dkParser.EnvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_env)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(dkParser.ENV)
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 151
                self.env_pair()
                pass

            elif la_ == 2:
                self.state = 152
                self.env_single()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(dkParser.ADD, 0)

        def path_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.Path_specContext)
            else:
                return self.getTypedRuleContext(dkParser.Path_specContext,i)


        def param_opt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.Param_optContext)
            else:
                return self.getTypedRuleContext(dkParser.Param_optContext,i)


        def getRuleIndex(self):
            return dkParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)




    def add(self):

        localctx = dkParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(dkParser.ADD)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 402653248) != 0):
                self.state = 156
                self.param_opt()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.path_spec()
            self.state = 163
            self.path_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CopyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COPY(self):
            return self.getToken(dkParser.COPY, 0)

        def path_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.Path_specContext)
            else:
                return self.getTypedRuleContext(dkParser.Path_specContext,i)


        def param_opt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.Param_optContext)
            else:
                return self.getTypedRuleContext(dkParser.Param_optContext,i)


        def getRuleIndex(self):
            return dkParser.RULE_copy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCopy" ):
                listener.enterCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCopy" ):
                listener.exitCopy(self)




    def copy(self):

        localctx = dkParser.CopyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_copy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(dkParser.COPY)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 402653248) != 0):
                self.state = 166
                self.param_opt()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.path_spec()
            self.state = 173
            self.path_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntrypointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTRYPOINT(self):
            return self.getToken(dkParser.ENTRYPOINT, 0)

        def json_command(self):
            return self.getTypedRuleContext(dkParser.Json_commandContext,0)


        def shell_command(self):
            return self.getTypedRuleContext(dkParser.Shell_commandContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_entrypoint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrypoint" ):
                listener.enterEntrypoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrypoint" ):
                listener.exitEntrypoint(self)




    def entrypoint(self):

        localctx = dkParser.EntrypointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_entrypoint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(dkParser.ENTRYPOINT)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 176
                self.json_command()
                pass
            elif token in [51]:
                self.state = 177
                self.shell_command()
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


    class VolumeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOLUME(self):
            return self.getToken(dkParser.VOLUME, 0)

        def json_array(self):
            return self.getTypedRuleContext(dkParser.Json_arrayContext,0)


        def shell_command_paths(self):
            return self.getTypedRuleContext(dkParser.Shell_command_pathsContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_volume

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVolume" ):
                listener.enterVolume(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVolume" ):
                listener.exitVolume(self)




    def volume(self):

        localctx = dkParser.VolumeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_volume)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(dkParser.VOLUME)
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 181
                self.json_array()
                pass
            elif token in [36, 38, 44, 45, 46, 47, 48, 49, 50]:
                self.state = 182
                self.shell_command_paths()
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


    class UserContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USER(self):
            return self.getToken(dkParser.USER, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def getRuleIndex(self):
            return dkParser.RULE_user

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUser" ):
                listener.enterUser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUser" ):
                listener.exitUser(self)




    def user(self):

        localctx = dkParser.UserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_user)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(dkParser.USER)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 186
                self.match(dkParser.WORD)
                pass

            elif la_ == 2:
                self.state = 187
                self.match(dkParser.WORD)
                self.state = 188
                self.match(dkParser.T__0)
                self.state = 189
                self.match(dkParser.WORD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WorkdirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORKDIR(self):
            return self.getToken(dkParser.WORKDIR, 0)

        def path_spec(self):
            return self.getTypedRuleContext(dkParser.Path_specContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_workdir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWorkdir" ):
                listener.enterWorkdir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWorkdir" ):
                listener.exitWorkdir(self)




    def workdir(self):

        localctx = dkParser.WorkdirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_workdir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(dkParser.WORKDIR)
            self.state = 193
            self.path_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARG(self):
            return self.getToken(dkParser.ARG, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def EQ(self):
            return self.getToken(dkParser.EQ, 0)

        def QUOTED_STRING(self):
            return self.getToken(dkParser.QUOTED_STRING, 0)

        def getRuleIndex(self):
            return dkParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)




    def arg(self):

        localctx = dkParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(dkParser.ARG)
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 196
                self.match(dkParser.WORD)
                pass

            elif la_ == 2:
                self.state = 197
                self.match(dkParser.WORD)
                self.state = 198
                self.match(dkParser.EQ)
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==36 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OnbuildContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONBUILD(self):
            return self.getToken(dkParser.ONBUILD, 0)

        def instruction(self):
            return self.getTypedRuleContext(dkParser.InstructionContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_onbuild

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOnbuild" ):
                listener.enterOnbuild(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOnbuild" ):
                listener.exitOnbuild(self)




    def onbuild(self):

        localctx = dkParser.OnbuildContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_onbuild)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(dkParser.ONBUILD)
            self.state = 203
            self.instruction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StopsignalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOPSIGNAL(self):
            return self.getToken(dkParser.STOPSIGNAL, 0)

        def WORD(self):
            return self.getToken(dkParser.WORD, 0)

        def getRuleIndex(self):
            return dkParser.RULE_stopsignal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStopsignal" ):
                listener.enterStopsignal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStopsignal" ):
                listener.exitStopsignal(self)




    def stopsignal(self):

        localctx = dkParser.StopsignalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stopsignal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(dkParser.STOPSIGNAL)
            self.state = 206
            self.match(dkParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HealthcheckContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEALTHCHECK(self):
            return self.getToken(dkParser.HEALTHCHECK, 0)

        def health_none(self):
            return self.getTypedRuleContext(dkParser.Health_noneContext,0)


        def health_cmd(self):
            return self.getTypedRuleContext(dkParser.Health_cmdContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_healthcheck

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHealthcheck" ):
                listener.enterHealthcheck(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHealthcheck" ):
                listener.exitHealthcheck(self)




    def healthcheck(self):

        localctx = dkParser.HealthcheckContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_healthcheck)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(dkParser.HEALTHCHECK)
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 209
                self.health_none()
                pass
            elif token in [8, 30, 31, 32, 33]:
                self.state = 210
                self.health_cmd()
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


    class ShellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHELL(self):
            return self.getToken(dkParser.SHELL, 0)

        def json_array(self):
            return self.getTypedRuleContext(dkParser.Json_arrayContext,0)


        def getRuleIndex(self):
            return dkParser.RULE_shell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShell" ):
                listener.enterShell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShell" ):
                listener.exitShell(self)




    def shell(self):

        localctx = dkParser.ShellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_shell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(dkParser.SHELL)
            self.state = 214
            self.json_array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Platform_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLATFORM(self):
            return self.getToken(dkParser.PLATFORM, 0)

        def WORD(self):
            return self.getToken(dkParser.WORD, 0)

        def getRuleIndex(self):
            return dkParser.RULE_platform_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlatform_opt" ):
                listener.enterPlatform_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlatform_opt" ):
                listener.exitPlatform_opt(self)




    def platform_opt(self):

        localctx = dkParser.Platform_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_platform_opt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(dkParser.PLATFORM)
            self.state = 217
            self.match(dkParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS(self):
            return self.getToken(dkParser.AS, 0)

        def WORD(self):
            return self.getToken(dkParser.WORD, 0)

        def getRuleIndex(self):
            return dkParser.RULE_as_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAs_opt" ):
                listener.enterAs_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAs_opt" ):
                listener.exitAs_opt(self)




    def as_opt(self):

        localctx = dkParser.As_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_as_opt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(dkParser.AS)
            self.state = 220
            self.match(dkParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(dkParser.NAME, 0)

        def EQ(self):
            return self.getToken(dkParser.EQ, 0)

        def WORD(self):
            return self.getToken(dkParser.WORD, 0)

        def getRuleIndex(self):
            return dkParser.RULE_name_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_opt" ):
                listener.enterName_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_opt" ):
                listener.exitName_opt(self)




    def name_opt(self):

        localctx = dkParser.Name_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_name_opt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(dkParser.NAME)
            self.state = 223
            self.match(dkParser.EQ)
            self.state = 224
            self.match(dkParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(dkParser.EQ, 0)

        def CHOWN(self):
            return self.getToken(dkParser.CHOWN, 0)

        def CHMOD(self):
            return self.getToken(dkParser.CHMOD, 0)

        def FROM(self):
            return self.getToken(dkParser.FROM, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def getRuleIndex(self):
            return dkParser.RULE_param_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_opt" ):
                listener.enterParam_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_opt" ):
                listener.exitParam_opt(self)




    def param_opt(self):

        localctx = dkParser.Param_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_param_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 402653248) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 227
            self.match(dkParser.EQ)
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 228
                self.match(dkParser.WORD)
                pass

            elif la_ == 2:
                self.state = 229
                self.match(dkParser.WORD)
                self.state = 230
                self.match(dkParser.T__0)
                self.state = 231
                self.match(dkParser.WORD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Image_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def getRuleIndex(self):
            return dkParser.RULE_image_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImage_spec" ):
                listener.enterImage_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImage_spec" ):
                listener.exitImage_spec(self)




    def image_spec(self):

        localctx = dkParser.Image_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_image_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(dkParser.WORD)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 235
                self.match(dkParser.T__0)
                self.state = 236
                self.match(dkParser.WORD)


            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 239
                self.match(dkParser.T__1)
                self.state = 240
                self.match(dkParser.WORD)
                self.state = 241
                self.match(dkParser.T__0)
                self.state = 242
                self.match(dkParser.WORD)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Label_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def EQ(self):
            return self.getToken(dkParser.EQ, 0)

        def QUOTED_STRING(self):
            return self.getToken(dkParser.QUOTED_STRING, 0)

        def getRuleIndex(self):
            return dkParser.RULE_label_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_pair" ):
                listener.enterLabel_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_pair" ):
                listener.exitLabel_pair(self)




    def label_pair(self):

        localctx = dkParser.Label_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_label_pair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(dkParser.WORD)
            self.state = 246
            self.match(dkParser.EQ)
            self.state = 247
            _la = self._input.LA(1)
            if not(_la==36 or _la==38):
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


    class Env_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def EQ(self):
            return self.getToken(dkParser.EQ, 0)

        def QUOTED_STRING(self):
            return self.getToken(dkParser.QUOTED_STRING, 0)

        def getRuleIndex(self):
            return dkParser.RULE_env_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_pair" ):
                listener.enterEnv_pair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_pair" ):
                listener.exitEnv_pair(self)




    def env_pair(self):

        localctx = dkParser.Env_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_env_pair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(dkParser.WORD)
            self.state = 250
            self.match(dkParser.EQ)
            self.state = 251
            _la = self._input.LA(1)
            if not(_la==36 or _la==38):
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


    class Env_singleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def QUOTED_STRING(self):
            return self.getToken(dkParser.QUOTED_STRING, 0)

        def getRuleIndex(self):
            return dkParser.RULE_env_single

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_single" ):
                listener.enterEnv_single(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_single" ):
                listener.exitEnv_single(self)




    def env_single(self):

        localctx = dkParser.Env_singleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_env_single)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(dkParser.WORD)
            self.state = 254
            _la = self._input.LA(1)
            if not(_la==36 or _la==38):
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


    class Path_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.WORD)
            else:
                return self.getToken(dkParser.WORD, i)

        def QUOTED_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.QUOTED_STRING)
            else:
                return self.getToken(dkParser.QUOTED_STRING, i)

        def TILDE(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.TILDE)
            else:
                return self.getToken(dkParser.TILDE, i)

        def POINT(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.POINT)
            else:
                return self.getToken(dkParser.POINT, i)

        def RSLASH(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.RSLASH)
            else:
                return self.getToken(dkParser.RSLASH, i)

        def DOLLAR(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.DOLLAR)
            else:
                return self.getToken(dkParser.DOLLAR, i)

        def ASTERISK(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.ASTERISK)
            else:
                return self.getToken(dkParser.ASTERISK, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.MINUS)
            else:
                return self.getToken(dkParser.MINUS, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.UNDERSCORE)
            else:
                return self.getToken(dkParser.UNDERSCORE, i)

        def getRuleIndex(self):
            return dkParser.RULE_path_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath_spec" ):
                listener.enterPath_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath_spec" ):
                listener.exitPath_spec(self)




    def path_spec(self):

        localctx = dkParser.Path_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_path_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 256
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2234551225024512) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 259 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shell_command_pathsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.Path_specContext)
            else:
                return self.getTypedRuleContext(dkParser.Path_specContext,i)


        def getRuleIndex(self):
            return dkParser.RULE_shell_command_paths

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShell_command_paths" ):
                listener.enterShell_command_paths(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShell_command_paths" ):
                listener.exitShell_command_paths(self)




    def shell_command_paths(self):

        localctx = dkParser.Shell_command_pathsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_shell_command_paths)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.path_spec()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234551225024512) != 0):
                self.state = 262
                self.path_spec()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Json_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(dkParser.LBRACKET, 0)

        def QUOTED_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.QUOTED_STRING)
            else:
                return self.getToken(dkParser.QUOTED_STRING, i)

        def RBRACKET(self):
            return self.getToken(dkParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.COMMA)
            else:
                return self.getToken(dkParser.COMMA, i)

        def getRuleIndex(self):
            return dkParser.RULE_json_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson_command" ):
                listener.enterJson_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson_command" ):
                listener.exitJson_command(self)




    def json_command(self):

        localctx = dkParser.Json_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_json_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(dkParser.LBRACKET)
            self.state = 269
            self.match(dkParser.QUOTED_STRING)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 270
                self.match(dkParser.COMMA)
                self.state = 271
                self.match(dkParser.QUOTED_STRING)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
            self.match(dkParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Json_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(dkParser.LBRACKET, 0)

        def QUOTED_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.QUOTED_STRING)
            else:
                return self.getToken(dkParser.QUOTED_STRING, i)

        def RBRACKET(self):
            return self.getToken(dkParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.COMMA)
            else:
                return self.getToken(dkParser.COMMA, i)

        def getRuleIndex(self):
            return dkParser.RULE_json_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson_array" ):
                listener.enterJson_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson_array" ):
                listener.exitJson_array(self)




    def json_array(self):

        localctx = dkParser.Json_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_json_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(dkParser.LBRACKET)
            self.state = 280
            self.match(dkParser.QUOTED_STRING)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 281
                self.match(dkParser.COMMA)
                self.state = 282
                self.match(dkParser.QUOTED_STRING)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self.match(dkParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shell_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY_CHAR_EXCEPT_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(dkParser.ANY_CHAR_EXCEPT_NEWLINE)
            else:
                return self.getToken(dkParser.ANY_CHAR_EXCEPT_NEWLINE, i)

        def getRuleIndex(self):
            return dkParser.RULE_shell_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShell_command" ):
                listener.enterShell_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShell_command" ):
                listener.exitShell_command(self)




    def shell_command(self):

        localctx = dkParser.Shell_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_shell_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 290
                self.match(dkParser.ANY_CHAR_EXCEPT_NEWLINE)
                self.state = 293 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Health_noneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(dkParser.NONE, 0)

        def getRuleIndex(self):
            return dkParser.RULE_health_none

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHealth_none" ):
                listener.enterHealth_none(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHealth_none" ):
                listener.exitHealth_none(self)




    def health_none(self):

        localctx = dkParser.Health_noneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_health_none)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(dkParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Health_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMD(self):
            return self.getToken(dkParser.CMD, 0)

        def json_command(self):
            return self.getTypedRuleContext(dkParser.Json_commandContext,0)


        def shell_command(self):
            return self.getTypedRuleContext(dkParser.Shell_commandContext,0)


        def options_opt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dkParser.Options_optContext)
            else:
                return self.getTypedRuleContext(dkParser.Options_optContext,i)


        def getRuleIndex(self):
            return dkParser.RULE_health_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHealth_cmd" ):
                listener.enterHealth_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHealth_cmd" ):
                listener.exitHealth_cmd(self)




    def health_cmd(self):

        localctx = dkParser.Health_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_health_cmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0):
                self.state = 297
                self.options_opt()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303
            self.match(dkParser.CMD)
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 304
                self.json_command()
                pass
            elif token in [51]:
                self.state = 305
                self.shell_command()
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


    class Options_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(dkParser.EQ, 0)

        def INTERVAL(self):
            return self.getToken(dkParser.INTERVAL, 0)

        def TIMEOUT(self):
            return self.getToken(dkParser.TIMEOUT, 0)

        def START_PERIOD(self):
            return self.getToken(dkParser.START_PERIOD, 0)

        def RETRIES(self):
            return self.getToken(dkParser.RETRIES, 0)

        def INTEGER(self):
            return self.getToken(dkParser.INTEGER, 0)

        def getRuleIndex(self):
            return dkParser.RULE_options_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptions_opt" ):
                listener.enterOptions_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptions_opt" ):
                listener.exitOptions_opt(self)




    def options_opt(self):

        localctx = dkParser.Options_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_options_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 309
            self.match(dkParser.EQ)

            self.state = 310
            self.match(dkParser.INTEGER)
            self.state = 311
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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





