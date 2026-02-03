# Generated from ./backend/grammar/Terraform.g4 by ANTLR 4.13.1
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
        4,1,19,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,26,8,1,
        1,1,1,1,1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,1,2,1,2,1,2,1,2,3,2,
        41,8,2,1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,4,1,4,1,4,1,4,5,4,54,
        8,4,10,4,12,4,57,9,4,3,4,59,8,4,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,4,
        6,8,10,0,2,2,0,12,12,16,16,1,0,12,16,67,0,16,1,0,0,0,2,21,1,0,0,
        0,4,29,1,0,0,0,6,46,1,0,0,0,8,49,1,0,0,0,10,62,1,0,0,0,12,15,3,4,
        2,0,13,15,3,2,1,0,14,12,1,0,0,0,14,13,1,0,0,0,15,18,1,0,0,0,16,14,
        1,0,0,0,16,17,1,0,0,0,17,19,1,0,0,0,18,16,1,0,0,0,19,20,5,0,0,1,
        20,1,1,0,0,0,21,22,5,16,0,0,22,25,5,7,0,0,23,26,3,10,5,0,24,26,3,
        8,4,0,25,23,1,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,28,5,17,0,0,28,
        3,1,0,0,0,29,33,5,16,0,0,30,32,7,0,0,0,31,30,1,0,0,0,32,35,1,0,0,
        0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,
        5,3,0,0,37,38,3,6,3,0,38,40,5,4,0,0,39,41,5,17,0,0,40,39,1,0,0,0,
        40,41,1,0,0,0,41,5,1,0,0,0,42,45,3,2,1,0,43,45,3,4,2,0,44,42,1,0,
        0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,7,
        1,0,0,0,48,46,1,0,0,0,49,58,5,5,0,0,50,55,3,10,5,0,51,52,5,8,0,0,
        52,54,3,10,5,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,
        0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,58,50,1,0,0,0,58,59,1,0,0,0,59,
        60,1,0,0,0,60,61,5,6,0,0,61,9,1,0,0,0,62,63,7,1,0,0,63,11,1,0,0,
        0,9,14,16,25,33,40,44,46,55,58
    ]

class TerraformParser ( Parser ):

    grammarFileName = "Terraform.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'", 
                     "'['", "']'", "'='", "','", "'#'", "'/'", "'*'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "MULTILINE_COMMENT", "LBRACE", 
                      "RBRACE", "LBRACKET", "RBRACKET", "EQ", "COMMA", "HASH", 
                      "RSLASH", "ASTERISK", "STRING", "INTEGER", "FLOAT", 
                      "BOOL", "WORD", "NEWLINE", "WS", "ANY_CHAR_EXCEPT_NEWLINE" ]

    RULE_file = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_body = 3
    RULE_list = 4
    RULE_value = 5

    ruleNames =  [ "file", "statement", "block", "body", "list", "value" ]

    EOF = Token.EOF
    COMMENT=1
    MULTILINE_COMMENT=2
    LBRACE=3
    RBRACE=4
    LBRACKET=5
    RBRACKET=6
    EQ=7
    COMMA=8
    HASH=9
    RSLASH=10
    ASTERISK=11
    STRING=12
    INTEGER=13
    FLOAT=14
    BOOL=15
    WORD=16
    NEWLINE=17
    WS=18
    ANY_CHAR_EXCEPT_NEWLINE=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TerraformParser.EOF, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformParser.BlockContext)
            else:
                return self.getTypedRuleContext(TerraformParser.BlockContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformParser.StatementContext)
            else:
                return self.getTypedRuleContext(TerraformParser.StatementContext,i)


        def getRuleIndex(self):
            return TerraformParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file_(self):

        localctx = TerraformParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 14
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.block()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.statement()
                    pass


                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(TerraformParser.EOF)
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

        def WORD(self):
            return self.getToken(TerraformParser.WORD, 0)

        def EQ(self):
            return self.getToken(TerraformParser.EQ, 0)

        def NEWLINE(self):
            return self.getToken(TerraformParser.NEWLINE, 0)

        def value(self):
            return self.getTypedRuleContext(TerraformParser.ValueContext,0)


        def list_(self):
            return self.getTypedRuleContext(TerraformParser.ListContext,0)


        def getRuleIndex(self):
            return TerraformParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = TerraformParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(TerraformParser.WORD)
            self.state = 22
            self.match(TerraformParser.EQ)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15, 16]:
                self.state = 23
                self.value()
                pass
            elif token in [5]:
                self.state = 24
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 27
            self.match(TerraformParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformParser.WORD)
            else:
                return self.getToken(TerraformParser.WORD, i)

        def LBRACE(self):
            return self.getToken(TerraformParser.LBRACE, 0)

        def body(self):
            return self.getTypedRuleContext(TerraformParser.BodyContext,0)


        def RBRACE(self):
            return self.getToken(TerraformParser.RBRACE, 0)

        def NEWLINE(self):
            return self.getToken(TerraformParser.NEWLINE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformParser.STRING)
            else:
                return self.getToken(TerraformParser.STRING, i)

        def getRuleIndex(self):
            return TerraformParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = TerraformParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(TerraformParser.WORD)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==16:
                self.state = 30
                _la = self._input.LA(1)
                if not(_la==12 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(TerraformParser.LBRACE)
            self.state = 37
            self.body()
            self.state = 38
            self.match(TerraformParser.RBRACE)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 39
                self.match(TerraformParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformParser.StatementContext)
            else:
                return self.getTypedRuleContext(TerraformParser.StatementContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformParser.BlockContext)
            else:
                return self.getTypedRuleContext(TerraformParser.BlockContext,i)


        def getRuleIndex(self):
            return TerraformParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = TerraformParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 44
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 42
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 43
                    self.block()
                    pass


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(TerraformParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(TerraformParser.RBRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformParser.ValueContext)
            else:
                return self.getTypedRuleContext(TerraformParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformParser.COMMA)
            else:
                return self.getToken(TerraformParser.COMMA, i)

        def getRuleIndex(self):
            return TerraformParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = TerraformParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(TerraformParser.LBRACKET)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0):
                self.state = 50
                self.value()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 51
                    self.match(TerraformParser.COMMA)
                    self.state = 52
                    self.value()
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 60
            self.match(TerraformParser.RBRACKET)
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

        def STRING(self):
            return self.getToken(TerraformParser.STRING, 0)

        def INTEGER(self):
            return self.getToken(TerraformParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(TerraformParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(TerraformParser.BOOL, 0)

        def WORD(self):
            return self.getToken(TerraformParser.WORD, 0)

        def getRuleIndex(self):
            return TerraformParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = TerraformParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
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





