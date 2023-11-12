import ASTlib
import ASTlib.parse as parser
import os
import json

file_test = '/examples/ex1.py'

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test
    jt = ASTlib.getAST(path)
    print(json.dumps(parser.data_from_module(jt), indent=4))