from antlr4 import *
from ParserProject02Lexer import ParserProject02Lexer
from ParserProject02Parser import ParserProject02Parser
from ParserProject02Listener import ParserProject02Listener

class DumpAssignments(ParserProject01Listener):
    def exitSimpleAssign(self, ctx:ParserProject02Parser.SimpleAssignContext):
        name = ctx.IDENT().getText()
        expr = ctx.expr().getText()
        print(f"{name} = {expr}")

    def exitAugAssign(self, ctx:ParserProject02Parser.AugAssignContext):
        name = ctx.IDENT().getText()
        op   = ctx.augOp().getText()
        expr = ctx.expr().getText()
        print(f"{name} {op} {expr}")

def main():
    stream = FileStream("project_deliverable_2.py", encoding="utf-8")
    lexer  = ParserProject01Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserProject01Parser(tokens)
    tree   = parser.prog()

    walker = ParseTreeWalker()
    walker.walk(DumpAssignments(), tree)

if __name__ == "__main__":
    main()

