from antlr4 import *
from ParserProject01Lexer import ParserProject01Lexer
from ParserProject01Parser import ParserProject01Parser
from ParserProject01Listener import ParserProject01Listener

class DumpAssignments(ParserProject01Listener):
    def exitSimpleAssign(self, ctx:ParserProject01Parser.SimpleAssignContext):
        name = ctx.IDENT().getText()
        expr = ctx.expr().getText()
        print(f"{name} = {expr}")

    def exitAugAssign(self, ctx:ParserProject01Parser.AugAssignContext):
        name = ctx.IDENT().getText()
        op   = ctx.augOp().getText()
        expr = ctx.expr().getText()
        print(f"{name} {op} {expr}")

def main():
    stream = FileStream("project_deliverable_1.py", encoding="utf-8")
    lexer  = ParserProject01Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserProject01Parser(tokens)
    tree   = parser.prog()

    walker = ParseTreeWalker()
    walker.walk(DumpAssignments(), tree)

if __name__ == "__main__":
    main()

