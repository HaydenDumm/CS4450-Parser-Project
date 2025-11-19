# Generated from ParserProject02.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserProject02Parser import ParserProject02Parser
else:
    from ParserProject02Parser import ParserProject02Parser

# This class defines a complete listener for a parse tree produced by ParserProject02Parser.
class ParserProject02Listener(ParseTreeListener):

    # Enter a parse tree produced by ParserProject02Parser#prog.
    def enterProg(self, ctx:ParserProject02Parser.ProgContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#prog.
    def exitProg(self, ctx:ParserProject02Parser.ProgContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#AssignStmt.
    def enterAssignStmt(self, ctx:ParserProject02Parser.AssignStmtContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#AssignStmt.
    def exitAssignStmt(self, ctx:ParserProject02Parser.AssignStmtContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#AugAssignStmt.
    def enterAugAssignStmt(self, ctx:ParserProject02Parser.AugAssignStmtContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#AugAssignStmt.
    def exitAugAssignStmt(self, ctx:ParserProject02Parser.AugAssignStmtContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#IfLogicStmt.
    def enterIfLogicStmt(self, ctx:ParserProject02Parser.IfLogicStmtContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#IfLogicStmt.
    def exitIfLogicStmt(self, ctx:ParserProject02Parser.IfLogicStmtContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#block.
    def enterBlock(self, ctx:ParserProject02Parser.BlockContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#block.
    def exitBlock(self, ctx:ParserProject02Parser.BlockContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#if_stmt.
    def enterIf_stmt(self, ctx:ParserProject02Parser.If_stmtContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#if_stmt.
    def exitIf_stmt(self, ctx:ParserProject02Parser.If_stmtContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#simpleAssign.
    def enterSimpleAssign(self, ctx:ParserProject02Parser.SimpleAssignContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#simpleAssign.
    def exitSimpleAssign(self, ctx:ParserProject02Parser.SimpleAssignContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#augAssign.
    def enterAugAssign(self, ctx:ParserProject02Parser.AugAssignContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#augAssign.
    def exitAugAssign(self, ctx:ParserProject02Parser.AugAssignContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#augOp.
    def enterAugOp(self, ctx:ParserProject02Parser.AugOpContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#augOp.
    def exitAugOp(self, ctx:ParserProject02Parser.AugOpContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#MulDivMod.
    def enterMulDivMod(self, ctx:ParserProject02Parser.MulDivModContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#MulDivMod.
    def exitMulDivMod(self, ctx:ParserProject02Parser.MulDivModContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#AddSub.
    def enterAddSub(self, ctx:ParserProject02Parser.AddSubContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#AddSub.
    def exitAddSub(self, ctx:ParserProject02Parser.AddSubContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#Comparison.
    def enterComparison(self, ctx:ParserProject02Parser.ComparisonContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#Comparison.
    def exitComparison(self, ctx:ParserProject02Parser.ComparisonContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#AndLogic.
    def enterAndLogic(self, ctx:ParserProject02Parser.AndLogicContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#AndLogic.
    def exitAndLogic(self, ctx:ParserProject02Parser.AndLogicContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#UnaryPlus.
    def enterUnaryPlus(self, ctx:ParserProject02Parser.UnaryPlusContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#UnaryPlus.
    def exitUnaryPlus(self, ctx:ParserProject02Parser.UnaryPlusContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#UnaryMinus.
    def enterUnaryMinus(self, ctx:ParserProject02Parser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#UnaryMinus.
    def exitUnaryMinus(self, ctx:ParserProject02Parser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#OrLogic.
    def enterOrLogic(self, ctx:ParserProject02Parser.OrLogicContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#OrLogic.
    def exitOrLogic(self, ctx:ParserProject02Parser.OrLogicContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#Atom.
    def enterAtom(self, ctx:ParserProject02Parser.AtomContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#Atom.
    def exitAtom(self, ctx:ParserProject02Parser.AtomContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#NotLogic.
    def enterNotLogic(self, ctx:ParserProject02Parser.NotLogicContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#NotLogic.
    def exitNotLogic(self, ctx:ParserProject02Parser.NotLogicContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#primary.
    def enterPrimary(self, ctx:ParserProject02Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#primary.
    def exitPrimary(self, ctx:ParserProject02Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#listLiteral.
    def enterListLiteral(self, ctx:ParserProject02Parser.ListLiteralContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#listLiteral.
    def exitListLiteral(self, ctx:ParserProject02Parser.ListLiteralContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#literal.
    def enterLiteral(self, ctx:ParserProject02Parser.LiteralContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#literal.
    def exitLiteral(self, ctx:ParserProject02Parser.LiteralContext):
        pass


    # Enter a parse tree produced by ParserProject02Parser#boolean_val.
    def enterBoolean_val(self, ctx:ParserProject02Parser.Boolean_valContext):
        pass

    # Exit a parse tree produced by ParserProject02Parser#boolean_val.
    def exitBoolean_val(self, ctx:ParserProject02Parser.Boolean_valContext):
        pass



del ParserProject02Parser