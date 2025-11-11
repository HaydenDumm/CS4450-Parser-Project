# Generated from ParserProject01.g4 by ANTLR 4.13.2
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
        4,1,21,107,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,4,0,26,8,0,
        11,0,12,0,27,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,1,1,1,5,1,
        40,8,1,10,1,12,1,43,9,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,3,1,
        52,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,70,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,
        9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,90,8,6,1,7,1,7,1,7,1,7,5,7,96,
        8,7,10,7,12,7,99,9,7,3,7,101,8,7,1,7,1,7,1,8,1,8,1,8,0,1,10,9,0,
        2,4,6,8,10,12,14,16,0,4,1,0,2,5,1,0,8,10,1,0,6,7,1,0,16,18,112,0,
        25,1,0,0,0,2,51,1,0,0,0,4,53,1,0,0,0,6,57,1,0,0,0,8,61,1,0,0,0,10,
        69,1,0,0,0,12,89,1,0,0,0,14,91,1,0,0,0,16,104,1,0,0,0,18,20,5,20,
        0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,
        1,0,0,0,23,21,1,0,0,0,24,26,3,2,1,0,25,21,1,0,0,0,26,27,1,0,0,0,
        27,25,1,0,0,0,27,28,1,0,0,0,28,32,1,0,0,0,29,31,5,20,0,0,30,29,1,
        0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,
        32,1,0,0,0,35,36,5,0,0,1,36,1,1,0,0,0,37,41,3,4,2,0,38,40,5,20,0,
        0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,52,
        1,0,0,0,43,41,1,0,0,0,44,48,3,6,3,0,45,47,5,20,0,0,46,45,1,0,0,0,
        47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,52,1,0,0,0,50,48,1,
        0,0,0,51,37,1,0,0,0,51,44,1,0,0,0,52,3,1,0,0,0,53,54,5,19,0,0,54,
        55,5,1,0,0,55,56,3,10,5,0,56,5,1,0,0,0,57,58,5,19,0,0,58,59,3,8,
        4,0,59,60,3,10,5,0,60,7,1,0,0,0,61,62,7,0,0,0,62,9,1,0,0,0,63,64,
        6,5,-1,0,64,65,5,6,0,0,65,70,3,10,5,5,66,67,5,7,0,0,67,70,3,10,5,
        4,68,70,3,12,6,0,69,63,1,0,0,0,69,66,1,0,0,0,69,68,1,0,0,0,70,79,
        1,0,0,0,71,72,10,3,0,0,72,73,7,1,0,0,73,78,3,10,5,4,74,75,10,2,0,
        0,75,76,7,2,0,0,76,78,3,10,5,3,77,71,1,0,0,0,77,74,1,0,0,0,78,81,
        1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,11,1,0,0,0,81,79,1,0,0,0,
        82,90,3,16,8,0,83,90,3,14,7,0,84,90,5,19,0,0,85,86,5,11,0,0,86,87,
        3,10,5,0,87,88,5,12,0,0,88,90,1,0,0,0,89,82,1,0,0,0,89,83,1,0,0,
        0,89,84,1,0,0,0,89,85,1,0,0,0,90,13,1,0,0,0,91,100,5,13,0,0,92,97,
        3,10,5,0,93,94,5,14,0,0,94,96,3,10,5,0,95,93,1,0,0,0,96,99,1,0,0,
        0,97,95,1,0,0,0,97,98,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,100,92,
        1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,103,5,15,0,0,103,15,
        1,0,0,0,104,105,7,3,0,0,105,17,1,0,0,0,12,21,27,32,41,48,51,69,77,
        79,89,97,100
    ]

class ParserProject01Parser ( Parser ):

    grammarFileName = "ParserProject01.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'-'", "'+'", "'*'", "'/'", "'%'", "'('", "')'", "'['", 
                     "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "STRING", "BOOL", "IDENT", "NL", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_simpleAssign = 2
    RULE_augAssign = 3
    RULE_augOp = 4
    RULE_expr = 5
    RULE_primary = 6
    RULE_listLiteral = 7
    RULE_literal = 8

    ruleNames =  [ "prog", "stmt", "simpleAssign", "augAssign", "augOp", 
                   "expr", "primary", "listLiteral", "literal" ]

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
    NUMBER=16
    STRING=17
    BOOL=18
    IDENT=19
    NL=20
    WS=21

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
            return self.getToken(ParserProject01Parser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject01Parser.StmtContext)
            else:
                return self.getTypedRuleContext(ParserProject01Parser.StmtContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject01Parser.NL)
            else:
                return self.getToken(ParserProject01Parser.NL, i)

        def getRuleIndex(self):
            return ParserProject01Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ParserProject01Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==20:
                        self.state = 18
                        self.match(ParserProject01Parser.NL)
                        self.state = 23
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 24
                    self.stmt()

                else:
                    raise NoViableAltException(self)
                self.state = 27 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 29
                self.match(ParserProject01Parser.NL)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(ParserProject01Parser.EOF)
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

        def simpleAssign(self):
            return self.getTypedRuleContext(ParserProject01Parser.SimpleAssignContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject01Parser.NL)
            else:
                return self.getToken(ParserProject01Parser.NL, i)

        def augAssign(self):
            return self.getTypedRuleContext(ParserProject01Parser.AugAssignContext,0)


        def getRuleIndex(self):
            return ParserProject01Parser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = ParserProject01Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.simpleAssign()
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 38
                        self.match(ParserProject01Parser.NL) 
                    self.state = 43
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.augAssign()
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 45
                        self.match(ParserProject01Parser.NL) 
                    self.state = 50
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass


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
            return self.getToken(ParserProject01Parser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProject01Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject01Parser.RULE_simpleAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssign" ):
                listener.enterSimpleAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssign" ):
                listener.exitSimpleAssign(self)




    def simpleAssign(self):

        localctx = ParserProject01Parser.SimpleAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simpleAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ParserProject01Parser.IDENT)
            self.state = 54
            self.match(ParserProject01Parser.T__0)
            self.state = 55
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
            return self.getToken(ParserProject01Parser.IDENT, 0)

        def augOp(self):
            return self.getTypedRuleContext(ParserProject01Parser.AugOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(ParserProject01Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject01Parser.RULE_augAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugAssign" ):
                listener.enterAugAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugAssign" ):
                listener.exitAugAssign(self)




    def augAssign(self):

        localctx = ParserProject01Parser.AugAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_augAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ParserProject01Parser.IDENT)
            self.state = 58
            self.augOp()
            self.state = 59
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
            return ParserProject01Parser.RULE_augOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugOp" ):
                listener.enterAugOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugOp" ):
                listener.exitAugOp(self)




    def augOp(self):

        localctx = ParserProject01Parser.AugOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_augOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
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
            return ParserProject01Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject01Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject01Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject01Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject01Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class UnaryPlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ParserProject01Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlus" ):
                listener.enterUnaryPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlus" ):
                listener.exitUnaryPlus(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ParserProject01Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)


    class AtomContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject01Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(ParserProject01Parser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserProject01Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = ParserProject01Parser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.match(ParserProject01Parser.T__5)
                self.state = 65
                self.expr(5)
                pass
            elif token in [7]:
                localctx = ParserProject01Parser.UnaryPlusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(ParserProject01Parser.T__6)
                self.state = 67
                self.expr(4)
                pass
            elif token in [11, 13, 16, 17, 18, 19]:
                localctx = ParserProject01Parser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ParserProject01Parser.MulDivModContext(self, ParserProject01Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 72
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 73
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = ParserProject01Parser.AddSubContext(self, ParserProject01Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 75
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 76
                        self.expr(3)
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            return self.getTypedRuleContext(ParserProject01Parser.LiteralContext,0)


        def listLiteral(self):
            return self.getTypedRuleContext(ParserProject01Parser.ListLiteralContext,0)


        def IDENT(self):
            return self.getToken(ParserProject01Parser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProject01Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject01Parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = ParserProject01Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primary)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.literal()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.listLiteral()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(ParserProject01Parser.IDENT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.match(ParserProject01Parser.T__10)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(ParserProject01Parser.T__11)
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
                return self.getTypedRuleContexts(ParserProject01Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject01Parser.ExprContext,i)


        def getRuleIndex(self):
            return ParserProject01Parser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)




    def listLiteral(self):

        localctx = ParserProject01Parser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ParserProject01Parser.T__12)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 993472) != 0):
                self.state = 92
                self.expr(0)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 93
                    self.match(ParserProject01Parser.T__13)
                    self.state = 94
                    self.expr(0)
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 102
            self.match(ParserProject01Parser.T__14)
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

        def BOOL(self):
            return self.getToken(ParserProject01Parser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ParserProject01Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ParserProject01Parser.STRING, 0)

        def getRuleIndex(self):
            return ParserProject01Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ParserProject01Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
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
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




