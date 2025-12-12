# CS4450-Parser-Project

GitHub Link: https://github.com/HaydenDumm/CS4450-Parser-Project.git

Project Description:
    This project implements a simplified Python 3 parser using ANTLR to recognize important aspects of the langauge.
    The grammar supports arithmetic expressions, assignments, conditionals, loops, nested structures, and comments, generating a complete parse tree for any valid input program.
    The goal is to imitate Python at simpler level to understand programming langauges in general and how their rules are used.

Members: Hayden Dummerth, Shane McKelvey, Collin Meyer, and Micheal Whaley

Requirments: 
    To run the parser, you need ANTLR 4, Python 3.10+ (or any Python 3.x), and the antlr4-python3-runtime library installed via pip.
    Setup involves generating the lexer and parser with "antlr4 -Dlanguage=Python3 [insert g4 file]", and running the parser scripts in a standard Python environment such as VS Code or a terminal.

How to Use:
    For each deliverable you can either use the run_parse python file or the run_parse_list file for a cleaner output.
    In order to run these files you will need to press the run button in VS Code or use the terminal by running the command "python3 [insert_run_parse_file]"
    The tree png is also provided with a white background now in Deliverable 3 to make it easier to view.
    To generate the tree we used the command "antlr4-parse ParserProject03.g4 prog -gui project_deliverable_3.py"

Demo Link:
    https://youtu.be/xrVjKb6uSqc
    I changed the tree in the video to have a white background so its visible.
    Also would like to add that you can run the programs with python3 in a terminal if you do not have vscode.
