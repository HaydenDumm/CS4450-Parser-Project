from antlr4 import *
from ParserProject01Lexer import ParserProject01Lexer
from ParserProject01Parser import ParserProject01Parser

def main():
    stream = FileStream("project_deliverable_1.py", encoding="utf-8")
    lexer = ParserProject01Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserProject01Parser(tokens)

    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
