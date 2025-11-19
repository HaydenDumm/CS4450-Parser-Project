// Generated from ParserProject02.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ParserProject02Parser}.
 */
public interface ParserProject02Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(ParserProject02Parser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(ParserProject02Parser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(ParserProject02Parser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(ParserProject02Parser.LineContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignStmt}
	 * labeled alternative in {@link ParserProject02Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignStmt(ParserProject02Parser.AssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignStmt}
	 * labeled alternative in {@link ParserProject02Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignStmt(ParserProject02Parser.AssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AugAssignStmt}
	 * labeled alternative in {@link ParserProject02Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterAugAssignStmt(ParserProject02Parser.AugAssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AugAssignStmt}
	 * labeled alternative in {@link ParserProject02Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitAugAssignStmt(ParserProject02Parser.AugAssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfLogicStmt}
	 * labeled alternative in {@link ParserProject02Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterIfLogicStmt(ParserProject02Parser.IfLogicStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfLogicStmt}
	 * labeled alternative in {@link ParserProject02Parser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitIfLogicStmt(ParserProject02Parser.IfLogicStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(ParserProject02Parser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(ParserProject02Parser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ParserProject02Parser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ParserProject02Parser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#simpleAssign}.
	 * @param ctx the parse tree
	 */
	void enterSimpleAssign(ParserProject02Parser.SimpleAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#simpleAssign}.
	 * @param ctx the parse tree
	 */
	void exitSimpleAssign(ParserProject02Parser.SimpleAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#augAssign}.
	 * @param ctx the parse tree
	 */
	void enterAugAssign(ParserProject02Parser.AugAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#augAssign}.
	 * @param ctx the parse tree
	 */
	void exitAugAssign(ParserProject02Parser.AugAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#augOp}.
	 * @param ctx the parse tree
	 */
	void enterAugOp(ParserProject02Parser.AugOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#augOp}.
	 * @param ctx the parse tree
	 */
	void exitAugOp(ParserProject02Parser.AugOpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDivMod}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDivMod(ParserProject02Parser.MulDivModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDivMod}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDivMod(ParserProject02Parser.MulDivModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(ParserProject02Parser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(ParserProject02Parser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterComparison(ParserProject02Parser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitComparison(ParserProject02Parser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AndLogic}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAndLogic(ParserProject02Parser.AndLogicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AndLogic}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAndLogic(ParserProject02Parser.AndLogicContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryPlus(ParserProject02Parser.UnaryPlusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryPlus(ParserProject02Parser.UnaryPlusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(ParserProject02Parser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(ParserProject02Parser.UnaryMinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OrLogic}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOrLogic(ParserProject02Parser.OrLogicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OrLogic}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOrLogic(ParserProject02Parser.OrLogicContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAtom(ParserProject02Parser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAtom(ParserProject02Parser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotLogic}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNotLogic(ParserProject02Parser.NotLogicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotLogic}
	 * labeled alternative in {@link ParserProject02Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNotLogic(ParserProject02Parser.NotLogicContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(ParserProject02Parser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(ParserProject02Parser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#listLiteral}.
	 * @param ctx the parse tree
	 */
	void enterListLiteral(ParserProject02Parser.ListLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#listLiteral}.
	 * @param ctx the parse tree
	 */
	void exitListLiteral(ParserProject02Parser.ListLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(ParserProject02Parser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(ParserProject02Parser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserProject02Parser#boolean_val}.
	 * @param ctx the parse tree
	 */
	void enterBoolean_val(ParserProject02Parser.Boolean_valContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserProject02Parser#boolean_val}.
	 * @param ctx the parse tree
	 */
	void exitBoolean_val(ParserProject02Parser.Boolean_valContext ctx);
}