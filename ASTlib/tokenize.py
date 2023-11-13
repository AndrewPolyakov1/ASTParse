import ast


class ListVisitor(ast.NodeVisitor):
    def __init__(self, indent=4):
        self.functions = []
        self.classes = []
        self.cur = 0
        self.ind = indent

    def visit_FunctionDef(self, node):
        print(f"{'':>{self.cur}}Function {node.name} {node.lineno}->{node.end_lineno}")

        self.functions.append({
            'name': node.name,
            'start': node.lineno,
            'end': node.end_lineno
        })

        self.cur += self.ind
        self.generic_visit(node)
        self.cur -= self.ind

    def visit_ClassDef(self, node):
        print(f"{'':>{self.cur}}Class {node.name} {node.lineno}->{node.end_lineno}")

        self.classes.append({
            'name': node.name,
            'start': node.lineno,
            'end': node.end_lineno
        })

        self.cur += self.ind
        self.generic_visit(node)
        self.cur -= self.ind

    def visit_nodes(self, fn: str):
        """
        Visits nodes of the AST, returning line number of the start and end of the functions. 

        Throws an exception on fail.

        Parameters
        ----------
        fn : str
            Filename of module to parse.

        Returns
        -------
        tuple[List, List]
            Tuple of two lists: classes and functions, containing the list of dicts of the following format:

            {
                'name': str,

                'start': int,

                'end': int

            }.
        """
        try:
            with open(fn) as source:
                self.visit(ast.parse(source.read(), filename=fn, mode='exec'))
        except SyntaxError as e:
            print(e)
        except OSError as e:
            print(e)
        return self.classes, self.functions


def tokenize(fn: str):
    """
    Tokenizes functions and classes in the module.

    Throws an exception on fail.

    Parameters
    ----------
    fn : str
        Filename of module to parse.

    Returns
    -------
    List
        A list of dicts with the following format:
            {
                "type": "function" / "class",
                "name": str,
                "code": str
            }
    """
    try:
        with open(fn) as source:
            lines = source.readlines()
    except SyntaxError as e:
        print(e)
    except OSError as e:
        print(e)

    v = ListVisitor()
    classes, functions = v.visit_nodes(fn)

    tokens = []

    for _func in functions:
        start = _func['start']
        end = _func['end']
        tokens.append({
            "type": "function",
            "name": _func['name'],
            "code": "".join(lines[start - 1: end])
        })

    for _cls in classes:
        start = _cls['start']
        end = _cls['end']
        tokens.append({
            "type": "class",
            "name": _cls['name'],
            "code": "".join(lines[start - 1: end])
        })

    return tokens


if __name__ == '__main__':
    import os
    import astlib
    import parse
    import json

    file_test = '/../examples/ex1.py'

    path = os.path.dirname(os.path.abspath(__file__))
    path += file_test
    jt = astlib.getAST(path)
    s = tokenize(path)
    print(json.dumps(s, indent=4))
