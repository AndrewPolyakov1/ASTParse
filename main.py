import ASTlib
import ASTlib.parse as parser
import os
import json
import ast
from py2cfg import CFGBuilder

file_test = '/examples/ex2.py'


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test
    jt = ASTlib.getAST(path)
    s = ASTlib.tokenize(path)
    for i, token in enumerate(s):
        print(f'[{__name__}] Token {i} -----------')
        print(ASTlib.translate(token['code']))
        # cfg = CFGBuilder().build_from_src(f".tmp/{token['type'].upper()} {token['name']}", token['code'])
        # cfg.build_visual(
        #     f'.tmp/exampleCFG_{i}', 
        #     'png', 
        #     build_keys=False,
        #     cleanup=False,
        #     show=False
        # )
