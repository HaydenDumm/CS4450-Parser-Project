# Generated from ParserProject02.g4 by ANTLR 4.13.2
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
        4,1,35,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,4,0,33,8,0,11,0,12,0,34,5,0,37,8,0,10,0,12,
        0,40,9,0,1,0,3,0,43,8,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,
        1,1,1,1,1,1,3,1,56,8,1,1,2,1,2,4,2,60,8,2,11,2,12,2,61,1,2,5,2,65,
        8,2,10,2,12,2,68,9,2,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,87,8,3,10,3,12,3,90,9,3,1,3,
        1,3,1,3,1,3,3,3,96,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,116,8,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,133,8,7,10,7,12,7,136,
        9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,145,8,8,1,9,1,9,1,9,1,9,5,9,
        151,8,9,10,9,12,9,154,9,9,3,9,156,8,9,1,9,1,9,1,10,1,10,1,10,3,10,
        163,8,10,1,11,1,11,1,11,0,1,14,12,0,2,4,6,8,10,12,14,16,18,20,22,
        0,5,1,0,3,6,1,0,9,11,1,0,7,8,1,0,12,17,1,0,26,27,181,0,27,1,0,0,
        0,2,55,1,0,0,0,4,57,1,0,0,0,6,75,1,0,0,0,8,97,1,0,0,0,10,101,1,0,
        0,0,12,105,1,0,0,0,14,115,1,0,0,0,16,144,1,0,0,0,18,146,1,0,0,0,
        20,162,1,0,0,0,22,164,1,0,0,0,24,26,5,34,0,0,25,24,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,38,1,0,0,0,29,27,1,0,0,0,
        30,32,3,2,1,0,31,33,5,34,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,
        0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,30,1,0,0,0,37,40,1,0,0,0,38,
        36,1,0,0,0,38,39,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,41,43,3,2,1,
        0,42,41,1,0,0,0,42,43,1,0,0,0,43,47,1,0,0,0,44,46,5,34,0,0,45,44,
        1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,
        49,47,1,0,0,0,50,51,5,0,0,1,51,1,1,0,0,0,52,56,3,8,4,0,53,56,3,10,
        5,0,54,56,3,6,3,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,3,
        1,0,0,0,57,66,3,2,1,0,58,60,5,34,0,0,59,58,1,0,0,0,60,61,1,0,0,0,
        61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,65,3,2,1,0,64,59,1,
        0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,72,1,0,0,0,68,
        66,1,0,0,0,69,71,5,34,0,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,
        0,0,72,73,1,0,0,0,73,5,1,0,0,0,74,72,1,0,0,0,75,76,5,23,0,0,76,77,
        3,14,7,0,77,78,5,1,0,0,78,79,5,34,0,0,79,88,3,4,2,0,80,81,5,24,0,
        0,81,82,3,14,7,0,82,83,5,1,0,0,83,84,5,34,0,0,84,85,3,4,2,0,85,87,
        1,0,0,0,86,80,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,95,1,0,0,0,90,88,1,0,0,0,91,92,5,25,0,0,92,93,5,1,0,0,93,94,5,
        34,0,0,94,96,3,4,2,0,95,91,1,0,0,0,95,96,1,0,0,0,96,7,1,0,0,0,97,
        98,5,33,0,0,98,99,5,2,0,0,99,100,3,14,7,0,100,9,1,0,0,0,101,102,
        5,33,0,0,102,103,3,12,6,0,103,104,3,14,7,0,104,11,1,0,0,0,105,106,
        7,0,0,0,106,13,1,0,0,0,107,108,6,7,-1,0,108,109,5,7,0,0,109,116,
        3,14,7,9,110,111,5,8,0,0,111,116,3,14,7,8,112,113,5,30,0,0,113,116,
        3,14,7,4,114,116,3,16,8,0,115,107,1,0,0,0,115,110,1,0,0,0,115,112,
        1,0,0,0,115,114,1,0,0,0,116,134,1,0,0,0,117,118,10,7,0,0,118,119,
        7,1,0,0,119,133,3,14,7,8,120,121,10,6,0,0,121,122,7,2,0,0,122,133,
        3,14,7,7,123,124,10,5,0,0,124,125,7,3,0,0,125,133,3,14,7,6,126,127,
        10,3,0,0,127,128,5,28,0,0,128,133,3,14,7,4,129,130,10,2,0,0,130,
        131,5,29,0,0,131,133,3,14,7,3,132,117,1,0,0,0,132,120,1,0,0,0,132,
        123,1,0,0,0,132,126,1,0,0,0,132,129,1,0,0,0,133,136,1,0,0,0,134,
        132,1,0,0,0,134,135,1,0,0,0,135,15,1,0,0,0,136,134,1,0,0,0,137,145,
        3,20,10,0,138,145,3,18,9,0,139,145,5,33,0,0,140,141,5,18,0,0,141,
        142,3,14,7,0,142,143,5,19,0,0,143,145,1,0,0,0,144,137,1,0,0,0,144,
        138,1,0,0,0,144,139,1,0,0,0,144,140,1,0,0,0,145,17,1,0,0,0,146,155,
        5,20,0,0,147,152,3,14,7,0,148,149,5,21,0,0,149,151,3,14,7,0,150,
        148,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,
        156,1,0,0,0,154,152,1,0,0,0,155,147,1,0,0,0,155,156,1,0,0,0,156,
        157,1,0,0,0,157,158,5,22,0,0,158,19,1,0,0,0,159,163,3,22,11,0,160,
        163,5,31,0,0,161,163,5,32,0,0,162,159,1,0,0,0,162,160,1,0,0,0,162,
        161,1,0,0,0,163,21,1,0,0,0,164,165,7,4,0,0,165,23,1,0,0,0,18,27,
        34,38,42,47,55,61,66,72,88,95,115,132,134,144,152,155,162
    ]

class ParserProject02Parser ( Parser ):

    grammarFileName = "ParserProject02.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'-'", "'+'", "'*'", "'/'", "'%'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'('", "')'", "'['", 
                     "','", "']'", "'if'", "'elif'", "'else'", "'True'", 
                     "'False'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "TRUE", "FALSE", "AND", "OR", "NOT", "NUMBER", 
                      "STRING", "IDENT", "NL", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_block = 2
    RULE_if_stmt = 3
    RULE_simpleAssign = 4
    RULE_augAssign = 5
    RULE_augOp = 6
    RULE_expr = 7
    RULE_primary = 8
    RULE_listLiteral = 9
    RULE_literal = 10
    RULE_boolean_val = 11

    ruleNames =  [ "prog", "stmt", "block", "if_stmt", "simpleAssign", "augAssign", 
                   "augOp", "expr", "primary", "listLiteral", "literal", 
                   "boolean_val" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    IF=23
    ELIF=24
    ELSE=25
    TRUE=26
    FALSE=27
    AND=28
    OR=29
    NOT=30
    NUMBER=31
    STRING=32
    IDENT=33
    NL=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ParserProject02Parser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject02Parser.NL)
            else:
                return self.getToken(ParserProject02Parser.NL, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.StmtContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.StmtContext,i)


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ParserProject02Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 24
                    self.match(ParserProject02Parser.NL) 
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self.stmt()
                    self.state = 32 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 31
                            self.match(ParserProject02Parser.NL)

                        else:
                            raise NoViableAltException(self)
                        self.state = 34 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23 or _la==33:
                self.state = 41
                self.stmt()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 44
                self.match(ParserProject02Parser.NL)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(ParserProject02Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AugAssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def augAssign(self):
            return self.getTypedRuleContext(ParserProject02Parser.AugAssignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugAssignStmt" ):
                listener.enterAugAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugAssignStmt" ):
                listener.exitAugAssignStmt(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simpleAssign(self):
            return self.getTypedRuleContext(ParserProject02Parser.SimpleAssignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)


    class IfLogicStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def if_stmt(self):
            return self.getTypedRuleContext(ParserProject02Parser.If_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfLogicStmt" ):
                listener.enterIfLogicStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfLogicStmt" ):
                listener.exitIfLogicStmt(self)



    def stmt(self):

        localctx = ParserProject02Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ParserProject02Parser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.simpleAssign()
                pass

            elif la_ == 2:
                localctx = ParserProject02Parser.AugAssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.augAssign()
                pass

            elif la_ == 3:
                localctx = ParserProject02Parser.IfLogicStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.if_stmt()
                pass


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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.StmtContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.StmtContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject02Parser.NL)
            else:
                return self.getToken(ParserProject02Parser.NL, i)

        def getRuleIndex(self):
            return ParserProject02Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ParserProject02Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.stmt()
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 58
                        self.match(ParserProject02Parser.NL)
                        self.state = 61 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==34):
                            break

                    self.state = 63
                    self.stmt() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.match(ParserProject02Parser.NL) 
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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

        def IF(self):
            return self.getToken(ParserProject02Parser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.ExprContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject02Parser.NL)
            else:
                return self.getToken(ParserProject02Parser.NL, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.BlockContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject02Parser.ELIF)
            else:
                return self.getToken(ParserProject02Parser.ELIF, i)

        def ELSE(self):
            return self.getToken(ParserProject02Parser.ELSE, 0)

        def getRuleIndex(self):
            return ParserProject02Parser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = ParserProject02Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ParserProject02Parser.IF)
            self.state = 76
            self.expr(0)
            self.state = 77
            self.match(ParserProject02Parser.T__0)
            self.state = 78
            self.match(ParserProject02Parser.NL)
            self.state = 79
            self.block()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self.match(ParserProject02Parser.ELIF)
                    self.state = 81
                    self.expr(0)
                    self.state = 82
                    self.match(ParserProject02Parser.T__0)
                    self.state = 83
                    self.match(ParserProject02Parser.NL)
                    self.state = 84
                    self.block() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(ParserProject02Parser.ELSE)
                self.state = 92
                self.match(ParserProject02Parser.T__0)
                self.state = 93
                self.match(ParserProject02Parser.NL)
                self.state = 94
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ParserProject02Parser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProject02Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_simpleAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssign" ):
                listener.enterSimpleAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssign" ):
                listener.exitSimpleAssign(self)




    def simpleAssign(self):

        localctx = ParserProject02Parser.SimpleAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simpleAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ParserProject02Parser.IDENT)
            self.state = 98
            self.match(ParserProject02Parser.T__1)
            self.state = 99
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AugAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ParserProject02Parser.IDENT, 0)

        def augOp(self):
            return self.getTypedRuleContext(ParserProject02Parser.AugOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(ParserProject02Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_augAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugAssign" ):
                listener.enterAugAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugAssign" ):
                listener.exitAugAssign(self)




    def augAssign(self):

        localctx = ParserProject02Parser.AugAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_augAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ParserProject02Parser.IDENT)
            self.state = 102
            self.augOp()
            self.state = 103
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AugOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_augOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugOp" ):
                listener.enterAugOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugOp" ):
                listener.exitAugOp(self)




    def augOp(self):

        localctx = ParserProject02Parser.AugOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_augOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)


    class AndLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.ExprContext,i)

        def AND(self):
            return self.getToken(ParserProject02Parser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndLogic" ):
                listener.enterAndLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndLogic" ):
                listener.exitAndLogic(self)


    class UnaryPlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ParserProject02Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlus" ):
                listener.enterUnaryPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlus" ):
                listener.exitUnaryPlus(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ParserProject02Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)


    class OrLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.ExprContext,i)

        def OR(self):
            return self.getToken(ParserProject02Parser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrLogic" ):
                listener.enterOrLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrLogic" ):
                listener.exitOrLogic(self)


    class AtomContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(ParserProject02Parser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)


    class NotLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject02Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ParserProject02Parser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserProject02Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotLogic" ):
                listener.enterNotLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotLogic" ):
                listener.exitNotLogic(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserProject02Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ParserProject02Parser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 108
                self.match(ParserProject02Parser.T__6)
                self.state = 109
                self.expr(9)
                pass
            elif token in [8]:
                localctx = ParserProject02Parser.UnaryPlusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(ParserProject02Parser.T__7)
                self.state = 111
                self.expr(8)
                pass
            elif token in [30]:
                localctx = ParserProject02Parser.NotLogicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(ParserProject02Parser.NOT)
                self.state = 113
                self.expr(4)
                pass
            elif token in [18, 20, 26, 27, 31, 32, 33]:
                localctx = ParserProject02Parser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 132
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = ParserProject02Parser.MulDivModContext(self, ParserProject02Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 117
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 118
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 119
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ParserProject02Parser.AddSubContext(self, ParserProject02Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 120
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 121
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 122
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ParserProject02Parser.ComparisonContext(self, ParserProject02Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 124
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 125
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = ParserProject02Parser.AndLogicContext(self, ParserProject02Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 126
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 127
                        self.match(ParserProject02Parser.AND)
                        self.state = 128
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = ParserProject02Parser.OrLogicContext(self, ParserProject02Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 130
                        self.match(ParserProject02Parser.OR)
                        self.state = 131
                        self.expr(3)
                        pass

             
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ParserProject02Parser.LiteralContext,0)


        def listLiteral(self):
            return self.getTypedRuleContext(ParserProject02Parser.ListLiteralContext,0)


        def IDENT(self):
            return self.getToken(ParserProject02Parser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProject02Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = ParserProject02Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primary)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.literal()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.listLiteral()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(ParserProject02Parser.IDENT)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.match(ParserProject02Parser.T__17)
                self.state = 141
                self.expr(0)
                self.state = 142
                self.match(ParserProject02Parser.T__18)
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


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject02Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject02Parser.ExprContext,i)


        def getRuleIndex(self):
            return ParserProject02Parser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)




    def listLiteral(self):

        localctx = ParserProject02Parser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ParserProject02Parser.T__19)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16308765056) != 0):
                self.state = 147
                self.expr(0)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 148
                    self.match(ParserProject02Parser.T__20)
                    self.state = 149
                    self.expr(0)
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 157
            self.match(ParserProject02Parser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_val(self):
            return self.getTypedRuleContext(ParserProject02Parser.Boolean_valContext,0)


        def NUMBER(self):
            return self.getToken(ParserProject02Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ParserProject02Parser.STRING, 0)

        def getRuleIndex(self):
            return ParserProject02Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ParserProject02Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.boolean_val()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(ParserProject02Parser.NUMBER)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.match(ParserProject02Parser.STRING)
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


    class Boolean_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ParserProject02Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ParserProject02Parser.FALSE, 0)

        def getRuleIndex(self):
            return ParserProject02Parser.RULE_boolean_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_val" ):
                listener.enterBoolean_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_val" ):
                listener.exitBoolean_val(self)




    def boolean_val(self):

        localctx = ParserProject02Parser.Boolean_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_boolean_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




