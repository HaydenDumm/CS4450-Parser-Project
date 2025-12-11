# CS4450-Parser-Project

Project Description:
    This project implements a simplified Python 3 parser using ANTLR to recognize important aspects of the langauge.
    The grammar supports arithmetic expressions, assignments, conditionals, loops, nested structures, and comments, generating a complete parse tree for any valid input program.
    The goal is to imitate Python at simpler level to understand programming langauges in general and how their rules are used.

Members:
    Hayden Dummerth
    Shane McKelvey
    Collin Meyer
    Micheal Whaley

Requirments: 
    To run the parser, you need ANTLR 4, Python 3.10+ (or any Python 3.x), and the antlr4-python3-runtime library installed via pip.
    Setup involves generating the lexer and parser with antlr4 -Dlanguage=Python3 [insert g4 file], and running the parser scripts in a standard Python environment such as VS Code or a terminal.

How to Use:
    For each deliverable you can either use the run_parse python file or the run_parse_list file for a cleaner output.
    The tree png is also provided with a white background now in Deliverable 3 (was transparent before).
    To generate the tree we used antlr4-parse ParserProject03.g4 prog -gui project_deliverable_3.py

Demo Link:
    https://youtu.be/xrVjKb6uSqc
    