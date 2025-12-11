# Generated from ParserProject03.g4 by ANTLR 4.13.2
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
        4,1,40,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,4,0,37,8,0,11,0,12,0,38,
        5,0,41,8,0,10,0,12,0,44,9,0,1,0,3,0,47,8,0,1,0,5,0,50,8,0,10,0,12,
        0,53,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,4,2,66,8,
        2,11,2,12,2,67,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,2,5,2,77,8,2,10,
        2,12,2,80,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,93,
        8,3,10,3,12,3,96,9,3,1,3,1,3,1,3,1,3,3,3,102,8,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,136,8,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,153,
        8,9,10,9,12,9,156,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,165,
        8,10,10,10,12,10,168,9,10,3,10,170,8,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,178,8,10,1,11,1,11,1,11,1,11,5,11,184,8,11,10,11,12,11,
        187,9,11,3,11,189,8,11,1,11,1,11,1,12,1,12,1,12,3,12,196,8,12,1,
        13,1,13,1,13,0,1,18,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,5,
        1,0,3,6,1,0,9,11,1,0,7,8,1,0,12,17,1,0,26,27,217,0,31,1,0,0,0,2,
        61,1,0,0,0,4,63,1,0,0,0,6,81,1,0,0,0,8,103,1,0,0,0,10,109,1,0,0,
        0,12,117,1,0,0,0,14,121,1,0,0,0,16,125,1,0,0,0,18,135,1,0,0,0,20,
        177,1,0,0,0,22,179,1,0,0,0,24,195,1,0,0,0,26,197,1,0,0,0,28,30,5,
        39,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,
        42,1,0,0,0,33,31,1,0,0,0,34,36,3,2,1,0,35,37,5,39,0,0,36,35,1,0,
        0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,34,
        1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,1,0,0,0,
        44,42,1,0,0,0,45,47,3,2,1,0,46,45,1,0,0,0,46,47,1,0,0,0,47,51,1,
        0,0,0,48,50,5,39,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,
        52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,1,1,0,0,
        0,56,62,3,12,6,0,57,62,3,14,7,0,58,62,3,6,3,0,59,62,3,8,4,0,60,62,
        3,10,5,0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,
        61,60,1,0,0,0,62,3,1,0,0,0,63,72,3,2,1,0,64,66,5,39,0,0,65,64,1,
        0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,
        71,3,2,1,0,70,65,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,
        0,73,78,1,0,0,0,74,72,1,0,0,0,75,77,5,39,0,0,76,75,1,0,0,0,77,80,
        1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,5,1,0,0,0,80,78,1,0,0,0,81,
        82,5,23,0,0,82,83,3,18,9,0,83,84,5,1,0,0,84,85,5,39,0,0,85,94,3,
        4,2,0,86,87,5,24,0,0,87,88,3,18,9,0,88,89,5,1,0,0,89,90,5,39,0,0,
        90,91,3,4,2,0,91,93,1,0,0,0,92,86,1,0,0,0,93,96,1,0,0,0,94,92,1,
        0,0,0,94,95,1,0,0,0,95,101,1,0,0,0,96,94,1,0,0,0,97,98,5,25,0,0,
        98,99,5,1,0,0,99,100,5,39,0,0,100,102,3,4,2,0,101,97,1,0,0,0,101,
        102,1,0,0,0,102,7,1,0,0,0,103,104,5,33,0,0,104,105,3,18,9,0,105,
        106,5,1,0,0,106,107,5,39,0,0,107,108,3,4,2,0,108,9,1,0,0,0,109,110,
        5,31,0,0,110,111,5,36,0,0,111,112,5,32,0,0,112,113,3,18,9,0,113,
        114,5,1,0,0,114,115,5,39,0,0,115,116,3,4,2,0,116,11,1,0,0,0,117,
        118,5,36,0,0,118,119,5,2,0,0,119,120,3,18,9,0,120,13,1,0,0,0,121,
        122,5,36,0,0,122,123,3,16,8,0,123,124,3,18,9,0,124,15,1,0,0,0,125,
        126,7,0,0,0,126,17,1,0,0,0,127,128,6,9,-1,0,128,129,5,7,0,0,129,
        136,3,18,9,9,130,131,5,8,0,0,131,136,3,18,9,8,132,133,5,30,0,0,133,
        136,3,18,9,4,134,136,3,20,10,0,135,127,1,0,0,0,135,130,1,0,0,0,135,
        132,1,0,0,0,135,134,1,0,0,0,136,154,1,0,0,0,137,138,10,7,0,0,138,
        139,7,1,0,0,139,153,3,18,9,8,140,141,10,6,0,0,141,142,7,2,0,0,142,
        153,3,18,9,7,143,144,10,5,0,0,144,145,7,3,0,0,145,153,3,18,9,6,146,
        147,10,3,0,0,147,148,5,28,0,0,148,153,3,18,9,4,149,150,10,2,0,0,
        150,151,5,29,0,0,151,153,3,18,9,3,152,137,1,0,0,0,152,140,1,0,0,
        0,152,143,1,0,0,0,152,146,1,0,0,0,152,149,1,0,0,0,153,156,1,0,0,
        0,154,152,1,0,0,0,154,155,1,0,0,0,155,19,1,0,0,0,156,154,1,0,0,0,
        157,178,3,24,12,0,158,178,3,22,11,0,159,160,5,36,0,0,160,169,5,18,
        0,0,161,166,3,18,9,0,162,163,5,19,0,0,163,165,3,18,9,0,164,162,1,
        0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,170,1,
        0,0,0,168,166,1,0,0,0,169,161,1,0,0,0,169,170,1,0,0,0,170,171,1,
        0,0,0,171,178,5,20,0,0,172,178,5,36,0,0,173,174,5,18,0,0,174,175,
        3,18,9,0,175,176,5,20,0,0,176,178,1,0,0,0,177,157,1,0,0,0,177,158,
        1,0,0,0,177,159,1,0,0,0,177,172,1,0,0,0,177,173,1,0,0,0,178,21,1,
        0,0,0,179,188,5,21,0,0,180,185,3,18,9,0,181,182,5,19,0,0,182,184,
        3,18,9,0,183,181,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,
        1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,188,180,1,0,0,0,188,189,
        1,0,0,0,189,190,1,0,0,0,190,191,5,22,0,0,191,23,1,0,0,0,192,196,
        3,26,13,0,193,196,5,34,0,0,194,196,5,35,0,0,195,192,1,0,0,0,195,
        193,1,0,0,0,195,194,1,0,0,0,196,25,1,0,0,0,197,198,7,4,0,0,198,27,
        1,0,0,0,20,31,38,42,46,51,61,67,72,78,94,101,135,152,154,166,169,
        177,185,188,195
    ]

class ParserProject03Parser ( Parser ):

    grammarFileName = "ParserProject03.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'-'", "'+'", "'*'", "'/'", "'%'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'('", "','", "')'", 
                     "'['", "']'", "'if'", "'elif'", "'else'", "'True'", 
                     "'False'", "'and'", "'or'", "'not'", "'for'", "'in'", 
                     "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "TRUE", "FALSE", "AND", "OR", "NOT", "FOR", 
                      "IN", "WHILE", "NUMBER", "STRING", "IDENT", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "NL", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_block = 2
    RULE_if_stmt = 3
    RULE_while_stmt = 4
    RULE_for_stmt = 5
    RULE_simpleAssign = 6
    RULE_augAssign = 7
    RULE_augOp = 8
    RULE_expr = 9
    RULE_primary = 10
    RULE_listLiteral = 11
    RULE_literal = 12
    RULE_boolean_val = 13

    ruleNames =  [ "prog", "stmt", "block", "if_stmt", "while_stmt", "for_stmt", 
                   "simpleAssign", "augAssign", "augOp", "expr", "primary", 
                   "listLiteral", "literal", "boolean_val" ]

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
    FOR=31
    IN=32
    WHILE=33
    NUMBER=34
    STRING=35
    IDENT=36
    BLOCK_COMMENT=37
    LINE_COMMENT=38
    NL=39
    WS=40

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
            return self.getToken(ParserProject03Parser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject03Parser.NL)
            else:
                return self.getToken(ParserProject03Parser.NL, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.StmtContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.StmtContext,i)


        def getRuleIndex(self):
            return ParserProject03Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ParserProject03Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self.match(ParserProject03Parser.NL) 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.stmt()
                    self.state = 36 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 35
                            self.match(ParserProject03Parser.NL)

                        else:
                            raise NoViableAltException(self)
                        self.state = 38 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 79465283584) != 0):
                self.state = 45
                self.stmt()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 48
                self.match(ParserProject03Parser.NL)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(ParserProject03Parser.EOF)
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
            return ParserProject03Parser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AugAssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def augAssign(self):
            return self.getTypedRuleContext(ParserProject03Parser.AugAssignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugAssignStmt" ):
                listener.enterAugAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugAssignStmt" ):
                listener.exitAugAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAugAssignStmt" ):
                return visitor.visitAugAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def while_stmt(self):
            return self.getTypedRuleContext(ParserProject03Parser.While_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simpleAssign(self):
            return self.getTypedRuleContext(ParserProject03Parser.SimpleAssignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class ForStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def for_stmt(self):
            return self.getTypedRuleContext(ParserProject03Parser.For_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfLogicStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def if_stmt(self):
            return self.getTypedRuleContext(ParserProject03Parser.If_stmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfLogicStmt" ):
                listener.enterIfLogicStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfLogicStmt" ):
                listener.exitIfLogicStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfLogicStmt" ):
                return visitor.visitIfLogicStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = ParserProject03Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = ParserProject03Parser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.simpleAssign()
                pass

            elif la_ == 2:
                localctx = ParserProject03Parser.AugAssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.augAssign()
                pass

            elif la_ == 3:
                localctx = ParserProject03Parser.IfLogicStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.if_stmt()
                pass

            elif la_ == 4:
                localctx = ParserProject03Parser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.while_stmt()
                pass

            elif la_ == 5:
                localctx = ParserProject03Parser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.for_stmt()
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
                return self.getTypedRuleContexts(ParserProject03Parser.StmtContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.StmtContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject03Parser.NL)
            else:
                return self.getToken(ParserProject03Parser.NL, i)

        def getRuleIndex(self):
            return ParserProject03Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ParserProject03Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.stmt()
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 65 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 64
                        self.match(ParserProject03Parser.NL)
                        self.state = 67 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==39):
                            break

                    self.state = 69
                    self.stmt() 
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.match(ParserProject03Parser.NL) 
                self.state = 80
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
            return self.getToken(ParserProject03Parser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject03Parser.NL)
            else:
                return self.getToken(ParserProject03Parser.NL, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.BlockContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ParserProject03Parser.ELIF)
            else:
                return self.getToken(ParserProject03Parser.ELIF, i)

        def ELSE(self):
            return self.getToken(ParserProject03Parser.ELSE, 0)

        def getRuleIndex(self):
            return ParserProject03Parser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ParserProject03Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(ParserProject03Parser.IF)
            self.state = 82
            self.expr(0)
            self.state = 83
            self.match(ParserProject03Parser.T__0)
            self.state = 84
            self.match(ParserProject03Parser.NL)
            self.state = 85
            self.block()
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.match(ParserProject03Parser.ELIF)
                    self.state = 87
                    self.expr(0)
                    self.state = 88
                    self.match(ParserProject03Parser.T__0)
                    self.state = 89
                    self.match(ParserProject03Parser.NL)
                    self.state = 90
                    self.block() 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 97
                self.match(ParserProject03Parser.ELSE)
                self.state = 98
                self.match(ParserProject03Parser.T__0)
                self.state = 99
                self.match(ParserProject03Parser.NL)
                self.state = 100
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ParserProject03Parser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProject03Parser.ExprContext,0)


        def NL(self):
            return self.getToken(ParserProject03Parser.NL, 0)

        def block(self):
            return self.getTypedRuleContext(ParserProject03Parser.BlockContext,0)


        def getRuleIndex(self):
            return ParserProject03Parser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = ParserProject03Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ParserProject03Parser.WHILE)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(ParserProject03Parser.T__0)
            self.state = 106
            self.match(ParserProject03Parser.NL)
            self.state = 107
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ParserProject03Parser.FOR, 0)

        def IDENT(self):
            return self.getToken(ParserProject03Parser.IDENT, 0)

        def IN(self):
            return self.getToken(ParserProject03Parser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProject03Parser.ExprContext,0)


        def NL(self):
            return self.getToken(ParserProject03Parser.NL, 0)

        def block(self):
            return self.getTypedRuleContext(ParserProject03Parser.BlockContext,0)


        def getRuleIndex(self):
            return ParserProject03Parser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ParserProject03Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ParserProject03Parser.FOR)
            self.state = 110
            self.match(ParserProject03Parser.IDENT)
            self.state = 111
            self.match(ParserProject03Parser.IN)
            self.state = 112
            self.expr(0)
            self.state = 113
            self.match(ParserProject03Parser.T__0)
            self.state = 114
            self.match(ParserProject03Parser.NL)
            self.state = 115
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
            return self.getToken(ParserProject03Parser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(ParserProject03Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject03Parser.RULE_simpleAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssign" ):
                listener.enterSimpleAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssign" ):
                listener.exitSimpleAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleAssign" ):
                return visitor.visitSimpleAssign(self)
            else:
                return visitor.visitChildren(self)




    def simpleAssign(self):

        localctx = ParserProject03Parser.SimpleAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simpleAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ParserProject03Parser.IDENT)
            self.state = 118
            self.match(ParserProject03Parser.T__1)
            self.state = 119
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
            return self.getToken(ParserProject03Parser.IDENT, 0)

        def augOp(self):
            return self.getTypedRuleContext(ParserProject03Parser.AugOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(ParserProject03Parser.ExprContext,0)


        def getRuleIndex(self):
            return ParserProject03Parser.RULE_augAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugAssign" ):
                listener.enterAugAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugAssign" ):
                listener.exitAugAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAugAssign" ):
                return visitor.visitAugAssign(self)
            else:
                return visitor.visitChildren(self)




    def augAssign(self):

        localctx = ParserProject03Parser.AugAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_augAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ParserProject03Parser.IDENT)
            self.state = 122
            self.augOp()
            self.state = 123
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
            return ParserProject03Parser.RULE_augOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAugOp" ):
                listener.enterAugOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAugOp" ):
                listener.exitAugOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAugOp" ):
                return visitor.visitAugOp(self)
            else:
                return visitor.visitChildren(self)




    def augOp(self):

        localctx = ParserProject03Parser.AugOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_augOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
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
            return ParserProject03Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class AndLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)

        def AND(self):
            return self.getToken(ParserProject03Parser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndLogic" ):
                listener.enterAndLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndLogic" ):
                listener.exitAndLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndLogic" ):
                return visitor.visitAndLogic(self)
            else:
                return visitor.visitChildren(self)


    class UnaryPlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ParserProject03Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlus" ):
                listener.enterUnaryPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlus" ):
                listener.exitUnaryPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryPlus" ):
                return visitor.visitUnaryPlus(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ParserProject03Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class OrLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)

        def OR(self):
            return self.getToken(ParserProject03Parser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrLogic" ):
                listener.enterOrLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrLogic" ):
                listener.exitOrLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrLogic" ):
                return visitor.visitOrLogic(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(ParserProject03Parser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)


    class NotLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserProject03Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ParserProject03Parser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(ParserProject03Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotLogic" ):
                listener.enterNotLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotLogic" ):
                listener.exitNotLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotLogic" ):
                return visitor.visitNotLogic(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ParserProject03Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ParserProject03Parser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 128
                self.match(ParserProject03Parser.T__6)
                self.state = 129
                self.expr(9)
                pass
            elif token in [8]:
                localctx = ParserProject03Parser.UnaryPlusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(ParserProject03Parser.T__7)
                self.state = 131
                self.expr(8)
                pass
            elif token in [30]:
                localctx = ParserProject03Parser.NotLogicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 132
                self.match(ParserProject03Parser.NOT)
                self.state = 133
                self.expr(4)
                pass
            elif token in [18, 21, 26, 27, 34, 35, 36]:
                localctx = ParserProject03Parser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 152
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = ParserProject03Parser.MulDivModContext(self, ParserProject03Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 137
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 138
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 139
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ParserProject03Parser.AddSubContext(self, ParserProject03Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 140
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 141
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 142
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ParserProject03Parser.ComparisonContext(self, ParserProject03Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 143
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 144
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 145
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = ParserProject03Parser.AndLogicContext(self, ParserProject03Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 146
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 147
                        self.match(ParserProject03Parser.AND)
                        self.state = 148
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = ParserProject03Parser.OrLogicContext(self, ParserProject03Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 149
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 150
                        self.match(ParserProject03Parser.OR)
                        self.state = 151
                        self.expr(3)
                        pass

             
                self.state = 156
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
            return self.getTypedRuleContext(ParserProject03Parser.LiteralContext,0)


        def listLiteral(self):
            return self.getTypedRuleContext(ParserProject03Parser.ListLiteralContext,0)


        def IDENT(self):
            return self.getToken(ParserProject03Parser.IDENT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)


        def getRuleIndex(self):
            return ParserProject03Parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = ParserProject03Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.listLiteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(ParserProject03Parser.IDENT)
                self.state = 160
                self.match(ParserProject03Parser.T__17)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 121536512384) != 0):
                    self.state = 161
                    self.expr(0)
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==19:
                        self.state = 162
                        self.match(ParserProject03Parser.T__18)
                        self.state = 163
                        self.expr(0)
                        self.state = 168
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 171
                self.match(ParserProject03Parser.T__19)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self.match(ParserProject03Parser.IDENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.match(ParserProject03Parser.T__17)
                self.state = 174
                self.expr(0)
                self.state = 175
                self.match(ParserProject03Parser.T__19)
                pass


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
                return self.getTypedRuleContexts(ParserProject03Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ParserProject03Parser.ExprContext,i)


        def getRuleIndex(self):
            return ParserProject03Parser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)




    def listLiteral(self):

        localctx = ParserProject03Parser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ParserProject03Parser.T__20)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 121536512384) != 0):
                self.state = 180
                self.expr(0)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
                    self.state = 181
                    self.match(ParserProject03Parser.T__18)
                    self.state = 182
                    self.expr(0)
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 190
            self.match(ParserProject03Parser.T__21)
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
            return self.getTypedRuleContext(ParserProject03Parser.Boolean_valContext,0)


        def NUMBER(self):
            return self.getToken(ParserProject03Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ParserProject03Parser.STRING, 0)

        def getRuleIndex(self):
            return ParserProject03Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ParserProject03Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.boolean_val()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(ParserProject03Parser.NUMBER)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.match(ParserProject03Parser.STRING)
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
            return self.getToken(ParserProject03Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ParserProject03Parser.FALSE, 0)

        def getRuleIndex(self):
            return ParserProject03Parser.RULE_boolean_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_val" ):
                listener.enterBoolean_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_val" ):
                listener.exitBoolean_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_val" ):
                return visitor.visitBoolean_val(self)
            else:
                return visitor.visitChildren(self)




    def boolean_val(self):

        localctx = ParserProject03Parser.Boolean_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_boolean_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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
        self._predicates[9] = self.expr_sempred
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
         




