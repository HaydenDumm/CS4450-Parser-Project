# Generated from ParserProject03.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserProject03Parser import ParserProject03Parser
else:
    from ParserProject03Parser import ParserProject03Parser

# This class defines a complete generic visitor for a parse tree produced by ParserProject03Parser.

class ParserProject03Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserProject03Parser#prog.
    def visitProg(self, ctx:ParserProject03Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#AssignStmt.
    def visitAssignStmt(self, ctx:ParserProject03Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#AugAssignStmt.
    def visitAugAssignStmt(self, ctx:ParserProject03Parser.AugAssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#IfLogicStmt.
    def visitIfLogicStmt(self, ctx:ParserProject03Parser.IfLogicStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#WhileStmt.
    def visitWhileStmt(self, ctx:ParserProject03Parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#ForStmt.
    def visitForStmt(self, ctx:ParserProject03Parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#block.
    def visitBlock(self, ctx:ParserProject03Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#if_stmt.
    def visitIf_stmt(self, ctx:ParserProject03Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#while_stmt.
    def visitWhile_stmt(self, ctx:ParserProject03Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#for_stmt.
    def visitFor_stmt(self, ctx:ParserProject03Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#simpleAssign.
    def visitSimpleAssign(self, ctx:ParserProject03Parser.SimpleAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#augAssign.
    def visitAugAssign(self, ctx:ParserProject03Parser.AugAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#augOp.
    def visitAugOp(self, ctx:ParserProject03Parser.AugOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#MulDivMod.
    def visitMulDivMod(self, ctx:ParserProject03Parser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#AddSub.
    def visitAddSub(self, ctx:ParserProject03Parser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#Comparison.
    def visitComparison(self, ctx:ParserProject03Parser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#AndLogic.
    def visitAndLogic(self, ctx:ParserProject03Parser.AndLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#UnaryPlus.
    def visitUnaryPlus(self, ctx:ParserProject03Parser.UnaryPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#UnaryMinus.
    def visitUnaryMinus(self, ctx:ParserProject03Parser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#OrLogic.
    def visitOrLogic(self, ctx:ParserProject03Parser.OrLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#Atom.
    def visitAtom(self, ctx:ParserProject03Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#NotLogic.
    def visitNotLogic(self, ctx:ParserProject03Parser.NotLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#primary.
    def visitPrimary(self, ctx:ParserProject03Parser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#listLiteral.
    def visitListLiteral(self, ctx:ParserProject03Parser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#literal.
    def visitLiteral(self, ctx:ParserProject03Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserProject03Parser#boolean_val.
    def visitBoolean_val(self, ctx:ParserProject03Parser.Boolean_valContext):
        return self.visitChildren(ctx)



del ParserProject03Parser