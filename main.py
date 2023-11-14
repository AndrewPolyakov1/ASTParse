import ASTlib
import ASTlib.parse as parser
import os
import json
import ast

file_test = '/examples/ex2.py'


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test
    jt = ASTlib.getAST(path)
    s = ASTlib.tokenize(path)
    for i, token in enumerate(s):
        print(f'[{__name__}] Token {i} -----------')
        print(ASTlib.translate(token['code']))
        ASTlib.create_image(f'.tmp/im{i}', token['code'])
        