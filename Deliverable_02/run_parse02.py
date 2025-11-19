from antlr4 import *
from ParserProject02Lexer import ParserProject02Lexer
from ParserProject02Parser import ParserProject02Parser

def main():
    stream = FileStream("project_deliverable_2.py", encoding="utf-8")
    lexer = ParserProject02Lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserProject02Parser(tokens)

    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
