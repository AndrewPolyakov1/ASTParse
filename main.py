import ASTlib
import ASTlib.parse as parser
import os
import json
import ast

file_test = '/examples/ex1.py'


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test
    jt = ASTlib.getAST(path)
    s = ASTlib.tokenize(path)
    print(json.dumps(s, indent=4))
