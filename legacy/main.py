import py2art
import os
import json
import ast
from PIL import Image
import io


file_test = '/examples/ex2.py'


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test
    s = py2art.tokenize(path)
    print(py2art.code_to_image_and_pseudocode(path))

    # for i, token in enumerate(s):
    #     cfg = ASTlib.CFGBuilder().build_from_src(f"{token['type'].upper()} {token['name']}", token['code'])
    #     pic_bytes = cfg.build_visual(
    #         None,# f'exampleCFG_{i}', 
    #         'png', 
    #         build_keys=False,
    #         show=False,
    #         calls=False,
    #         includeDefs=False
    #     )
    #     print(f'[{__name__}] Token {i} -----------')
    #     print(ASTlib.translate(token['code']))
    #     ASTlib.create_image(token['code']).show()
        
