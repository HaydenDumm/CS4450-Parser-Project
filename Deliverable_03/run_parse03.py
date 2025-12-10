from antlr4 import *
from ParserProject03Lexer import ParserProject03Lexer
from ParserProject03Parser import ParserProject03Parser

def main():
    stream = FileStream("Deliverable_03/project_deliverable_3.py", encoding="utf-8")
    lexer = ParserProject03Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserProject03Parser(tokens)

    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
