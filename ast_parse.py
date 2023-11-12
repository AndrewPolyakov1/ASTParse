import ast
import os
from ast2json import ast2json
import json
import ASTlib.parse as parser

file_test = '/examples/ex1.py'


def readFile(filename):
    text_file = open(filename, "r")

    # read whole file to a string
    data = text_file.read()

    # close file
    text_file.close()
    return data


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test

    data = readFile(path)
    t = ast.parse(data)
    jt = ast2json(t)

    # tree = parse_json(jt)
    # print_tree(tree)

    # print(json.dumps(jt, indent=4))
    print(json.dumps(parser.data_from_module(jt), indent=4))

    # print(ast.dump(t, indent=4))
