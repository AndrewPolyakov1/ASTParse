import os
from ast2json import ast2json
import ast


def _readFile(filename):
    '''
    Read file and return the string of contents

    Parameters
    ----------
    path : str
        Path to the file.
    '''
    _file = open(filename, "r")
    # read whole file to a string
    _data = _file.read()
    # close file
    _file.close()
    return _data


def getAST(path):
    '''
    Read file and return the python dict of given AST

    Parameters
    ----------
    path : str
        Path to the file.
    '''
    __data = _readFile(path)
    t = ast.parse(__data)
    __jt = ast2json(t)
    return __jt
