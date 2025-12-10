from antlr4 import *
from ParserProject03Lexer import ParserProject03Lexer
from ParserProject03Parser import ParserProject03Parser
from ParserProject03Listener import ParserProject03Listener

class DumpAssignments(ParserProject03Listener):
    def exitSimpleAssign(self, ctx:ParserProject03Parser.SimpleAssignContext):
        name = ctx.IDENT().getText()
        expr = ctx.expr().getText()
        print(f"{name} = {expr}")

    def exitAugAssign(self, ctx:ParserProject03Parser.AugAssignContext):
        name = ctx.IDENT().getText()
        op   = ctx.augOp().getText()
        expr = ctx.expr().getText()
        print(f"{name} {op} {expr}")

def main():
    stream = FileStream("Deliverable_03/project_deliverable_3.py", encoding="utf-8")
    lexer  = ParserProject03Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserProject03Parser(tokens)
    tree   = parser.prog()

    walker = ParseTreeWalker()
    walker.walk(DumpAssignments(), tree)

if __name__ == "__main__":
    main()

