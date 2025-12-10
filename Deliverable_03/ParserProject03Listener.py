# Generated from Deliverable_03/ParserProject03.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserProject03Parser import ParserProject03Parser
else:
    from ParserProject03Parser import ParserProject03Parser

# This class defines a complete listener for a parse tree produced by ParserProject03Parser.
class ParserProject03Listener(ParseTreeListener):

    # Enter a parse tree produced by ParserProject03Parser#prog.
    def enterProg(self, ctx:ParserProject03Parser.ProgContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#prog.
    def exitProg(self, ctx:ParserProject03Parser.ProgContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#AssignStmt.
    def enterAssignStmt(self, ctx:ParserProject03Parser.AssignStmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#AssignStmt.
    def exitAssignStmt(self, ctx:ParserProject03Parser.AssignStmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#AugAssignStmt.
    def enterAugAssignStmt(self, ctx:ParserProject03Parser.AugAssignStmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#AugAssignStmt.
    def exitAugAssignStmt(self, ctx:ParserProject03Parser.AugAssignStmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#IfLogicStmt.
    def enterIfLogicStmt(self, ctx:ParserProject03Parser.IfLogicStmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#IfLogicStmt.
    def exitIfLogicStmt(self, ctx:ParserProject03Parser.IfLogicStmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#WhileStmt.
    def enterWhileStmt(self, ctx:ParserProject03Parser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#WhileStmt.
    def exitWhileStmt(self, ctx:ParserProject03Parser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#ForStmt.
    def enterForStmt(self, ctx:ParserProject03Parser.ForStmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#ForStmt.
    def exitForStmt(self, ctx:ParserProject03Parser.ForStmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#block.
    def enterBlock(self, ctx:ParserProject03Parser.BlockContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#block.
    def exitBlock(self, ctx:ParserProject03Parser.BlockContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#if_stmt.
    def enterIf_stmt(self, ctx:ParserProject03Parser.If_stmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#if_stmt.
    def exitIf_stmt(self, ctx:ParserProject03Parser.If_stmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#while_stmt.
    def enterWhile_stmt(self, ctx:ParserProject03Parser.While_stmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#while_stmt.
    def exitWhile_stmt(self, ctx:ParserProject03Parser.While_stmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#for_stmt.
    def enterFor_stmt(self, ctx:ParserProject03Parser.For_stmtContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#for_stmt.
    def exitFor_stmt(self, ctx:ParserProject03Parser.For_stmtContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#simpleAssign.
    def enterSimpleAssign(self, ctx:ParserProject03Parser.SimpleAssignContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#simpleAssign.
    def exitSimpleAssign(self, ctx:ParserProject03Parser.SimpleAssignContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#augAssign.
    def enterAugAssign(self, ctx:ParserProject03Parser.AugAssignContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#augAssign.
    def exitAugAssign(self, ctx:ParserProject03Parser.AugAssignContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#augOp.
    def enterAugOp(self, ctx:ParserProject03Parser.AugOpContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#augOp.
    def exitAugOp(self, ctx:ParserProject03Parser.AugOpContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#MulDivMod.
    def enterMulDivMod(self, ctx:ParserProject03Parser.MulDivModContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#MulDivMod.
    def exitMulDivMod(self, ctx:ParserProject03Parser.MulDivModContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#AddSub.
    def enterAddSub(self, ctx:ParserProject03Parser.AddSubContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#AddSub.
    def exitAddSub(self, ctx:ParserProject03Parser.AddSubContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#Comparison.
    def enterComparison(self, ctx:ParserProject03Parser.ComparisonContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#Comparison.
    def exitComparison(self, ctx:ParserProject03Parser.ComparisonContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#AndLogic.
    def enterAndLogic(self, ctx:ParserProject03Parser.AndLogicContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#AndLogic.
    def exitAndLogic(self, ctx:ParserProject03Parser.AndLogicContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#UnaryPlus.
    def enterUnaryPlus(self, ctx:ParserProject03Parser.UnaryPlusContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#UnaryPlus.
    def exitUnaryPlus(self, ctx:ParserProject03Parser.UnaryPlusContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#UnaryMinus.
    def enterUnaryMinus(self, ctx:ParserProject03Parser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#UnaryMinus.
    def exitUnaryMinus(self, ctx:ParserProject03Parser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#OrLogic.
    def enterOrLogic(self, ctx:ParserProject03Parser.OrLogicContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#OrLogic.
    def exitOrLogic(self, ctx:ParserProject03Parser.OrLogicContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#Atom.
    def enterAtom(self, ctx:ParserProject03Parser.AtomContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#Atom.
    def exitAtom(self, ctx:ParserProject03Parser.AtomContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#NotLogic.
    def enterNotLogic(self, ctx:ParserProject03Parser.NotLogicContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#NotLogic.
    def exitNotLogic(self, ctx:ParserProject03Parser.NotLogicContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#primary.
    def enterPrimary(self, ctx:ParserProject03Parser.PrimaryContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#primary.
    def exitPrimary(self, ctx:ParserProject03Parser.PrimaryContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#listLiteral.
    def enterListLiteral(self, ctx:ParserProject03Parser.ListLiteralContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#listLiteral.
    def exitListLiteral(self, ctx:ParserProject03Parser.ListLiteralContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#literal.
    def enterLiteral(self, ctx:ParserProject03Parser.LiteralContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#literal.
    def exitLiteral(self, ctx:ParserProject03Parser.LiteralContext):
        pass


    # Enter a parse tree produced by ParserProject03Parser#boolean_val.
    def enterBoolean_val(self, ctx:ParserProject03Parser.Boolean_valContext):
        pass

    # Exit a parse tree produced by ParserProject03Parser#boolean_val.
    def exitBoolean_val(self, ctx:ParserProject03Parser.Boolean_valContext):
        pass



del ParserProject03Parser