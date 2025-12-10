// Generated from Deliverable_03/ParserProject03.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ParserProject03Parser}.
 */
public interface ParserProject03Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(ParserProject03Parser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(ParserProject03Parser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignStmt(ParserProject03Parser.AssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignStmt(ParserProject03Parser.AssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AugAssignStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterAugAssignStmt(ParserProject03Parser.AugAssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AugAssignStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitAugAssignStmt(ParserProject03Parser.AugAssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfLogicStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterIfLogicStmt(ParserProject03Parser.IfLogicStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfLogicStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitIfLogicStmt(ParserProject03Parser.IfLogicStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code WhileStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(ParserProject03Parser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code WhileStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(ParserProject03Parser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(ParserProject03Parser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForStmt}
	 * labeled alternative in {@link ParserProject03Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(ParserProject03Parser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ParserProject03Parser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ParserProject03Parser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(ParserProject03Parser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(ParserProject03Parser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(ParserProject03Parser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(ParserProject03Parser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(ParserProject03Parser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(ParserProject03Parser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#simpleAssign}.
	 * @param ctx the parse tree
	 */
	void enterSimpleAssign(ParserProject03Parser.SimpleAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#simpleAssign}.
	 * @param ctx the parse tree
	 */
	void exitSimpleAssign(ParserProject03Parser.SimpleAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#augAssign}.
	 * @param ctx the parse tree
	 */
	void enterAugAssign(ParserProject03Parser.AugAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#augAssign}.
	 * @param ctx the parse tree
	 */
	void exitAugAssign(ParserProject03Parser.AugAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#augOp}.
	 * @param ctx the parse tree
	 */
	void enterAugOp(ParserProject03Parser.AugOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#augOp}.
	 * @param ctx the parse tree
	 */
	void exitAugOp(ParserProject03Parser.AugOpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDivMod}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDivMod(ParserProject03Parser.MulDivModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDivMod}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDivMod(ParserProject03Parser.MulDivModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(ParserProject03Parser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(ParserProject03Parser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterComparison(ParserProject03Parser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitComparison(ParserProject03Parser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AndLogic}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAndLogic(ParserProject03Parser.AndLogicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AndLogic}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAndLogic(ParserProject03Parser.AndLogicContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryPlus(ParserProject03Parser.UnaryPlusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryPlus(ParserProject03Parser.UnaryPlusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(ParserProject03Parser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(ParserProject03Parser.UnaryMinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OrLogic}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOrLogic(ParserProject03Parser.OrLogicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OrLogic}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOrLogic(ParserProject03Parser.OrLogicContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAtom(ParserProject03Parser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAtom(ParserProject03Parser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotLogic}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNotLogic(ParserProject03Parser.NotLogicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotLogic}
	 * labeled alternative in {@link ParserProject03Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNotLogic(ParserProject03Parser.NotLogicContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(ParserProject03Parser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(ParserProject03Parser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#listLiteral}.
	 * @param ctx the parse tree
	 */
	void enterListLiteral(ParserProject03Parser.ListLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#listLiteral}.
	 * @param ctx the parse tree
	 */
	void exitListLiteral(ParserProject03Parser.ListLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(ParserProject03Parser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(ParserProject03Parser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject03Parser#boolean_val}.
	 * @param ctx the parse tree
	 */
	void enterBoolean_val(ParserProject03Parser.Boolean_valContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject03Parser#boolean_val}.
	 * @param ctx the parse tree
	 */
	void exitBoolean_val(ParserProject03Parser.Boolean_valContext ctx);
}