import ASTlib
import ASTlib.parse as parser
import os
import json
import ast
from py2cfg import CFGBuilder

file_test = '/examples/ex1.py'


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test
    jt = ASTlib.getAST(path)
    s = ASTlib.tokenize(path)
    for i, token in enumerate(s):
        cfg = CFGBuilder().build_from_src(f"{token['type'].upper()} {token['name']}", token['code'])
        cfg.build_visual(
            f'exampleCFG_{i}', 
            'png', 
            build_keys=False,
            show=False
        )
