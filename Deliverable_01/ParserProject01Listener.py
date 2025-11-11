# Generated from ParserProject01.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserProject01Parser import ParserProject01Parser
else:
    from ParserProject01Parser import ParserProject01Parser

# This class defines a complete listener for a parse tree produced by ParserProject01Parser.
class ParserProject01Listener(ParseTreeListener):

    # Enter a parse tree produced by ParserProject01Parser#prog.
    def enterProg(self, ctx:ParserProject01Parser.ProgContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#prog.
    def exitProg(self, ctx:ParserProject01Parser.ProgContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#stmt.
    def enterStmt(self, ctx:ParserProject01Parser.StmtContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#stmt.
    def exitStmt(self, ctx:ParserProject01Parser.StmtContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#simpleAssign.
    def enterSimpleAssign(self, ctx:ParserProject01Parser.SimpleAssignContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#simpleAssign.
    def exitSimpleAssign(self, ctx:ParserProject01Parser.SimpleAssignContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#augAssign.
    def enterAugAssign(self, ctx:ParserProject01Parser.AugAssignContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#augAssign.
    def exitAugAssign(self, ctx:ParserProject01Parser.AugAssignContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#augOp.
    def enterAugOp(self, ctx:ParserProject01Parser.AugOpContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#augOp.
    def exitAugOp(self, ctx:ParserProject01Parser.AugOpContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#MulDivMod.
    def enterMulDivMod(self, ctx:ParserProject01Parser.MulDivModContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#MulDivMod.
    def exitMulDivMod(self, ctx:ParserProject01Parser.MulDivModContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#AddSub.
    def enterAddSub(self, ctx:ParserProject01Parser.AddSubContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#AddSub.
    def exitAddSub(self, ctx:ParserProject01Parser.AddSubContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#UnaryPlus.
    def enterUnaryPlus(self, ctx:ParserProject01Parser.UnaryPlusContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#UnaryPlus.
    def exitUnaryPlus(self, ctx:ParserProject01Parser.UnaryPlusContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#UnaryMinus.
    def enterUnaryMinus(self, ctx:ParserProject01Parser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#UnaryMinus.
    def exitUnaryMinus(self, ctx:ParserProject01Parser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#Atom.
    def enterAtom(self, ctx:ParserProject01Parser.AtomContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#Atom.
    def exitAtom(self, ctx:ParserProject01Parser.AtomContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#primary.
    def enterPrimary(self, ctx:ParserProject01Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#primary.
    def exitPrimary(self, ctx:ParserProject01Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#listLiteral.
    def enterListLiteral(self, ctx:ParserProject01Parser.ListLiteralContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#listLiteral.
    def exitListLiteral(self, ctx:ParserProject01Parser.ListLiteralContext):
        pass


    # Enter a parse tree produced by ParserProject01Parser#literal.
    def enterLiteral(self, ctx:ParserProject01Parser.LiteralContext):
        pass

    # Exit a parse tree produced by ParserProject01Parser#literal.
    def exitLiteral(self, ctx:ParserProject01Parser.LiteralContext):
        pass



del ParserProject01Parser