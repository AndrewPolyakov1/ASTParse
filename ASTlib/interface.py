import graphviz as gv
from .pseudo import parse, unparse
from .tokenize import tokenize
from .py2cfg_ext import CFGBuilder
from PIL import Image
import io
import ast

node_styles = {
        "input": ("parallelogram", "#afeeee"),  # Pale Turquoise
        "default": ("rectangle", "#FFFB81"),  # Pale Yellow
        ast.If: ("diamond", "#FF6752"),  # Pale Red
        ast.For: ("hexagon", "#FFBE52"),  # Pale Orange
        ast.While: ("hexagon", "#FFBE52"),  # Pale Orange
        ast.Call: ("tab", "#E552FF"),  # Pale Purple
        ast.Return: ("parallelogram", "#98fb98"),  # Pale Green
        ast.Try: ("Mdiamond", "orange"),
        ast.Raise: ("house", "#98fb98"),
    }



# def build_cfg_config(code: str):
#     raise NotImplementedError


def build_cfg_config_file(code: str, name: str):
    raise NotImplementedError


def create_image_from_file(path: str, name: str):
    with open(path, 'r') as f:
        source = f.read()
        create_image_from_config(source, name)


def create_image_from_config(config: str, format: str) -> Image:
    graph = gv.Source(config)
    return Image.open(io.BytesIO(graph.pipe(format=format)))


# def wrapper_image(code: str, name: str):
#     config = build_cfg_config(code)
#     return create_image_from_config(config, name)


def build_cfg_config(code: str) -> str:
    """
    Get the CFG config of the code 

    Parameters
    ----------
    filepath : str
        Filename of module to parse.

    Returns
    -------
    config: str
        .dot file config
    """
    cfg = CFGBuilder().build_from_src('', code)
    src = cfg.build_source(
        'png',
        build_keys=False,
        show=False,
        calls=False,
        cleanup=False,
        includeDefs=False
    )
    return src


def translate(code: str) -> str:
    """
    Translate code into pseudocode

    Parameters
    ----------
    filepath : str
        Filename of module to parse.

    Returns
    -------
    str
        Code translated to Pseudocode
    """
    tree = parse(code)
    unparsed_code = unparse(tree)
    return unparsed_code


def code_to_image_and_pseudocode(filepath: str):
    """
    Returns List of tuples of format
        (name: str, code: str, Image, config: str)

    Parameters
    ----------
    filepath : str
        Filename of module to parse.

    Returns
    -------
    tuples: List
        List[(name: str, code: str, Image, config: str)]
    """
    tokens = tokenize(filepath)
    tuples = []
    for token in tokens:
        _pseudo = translate(token['code'])
        _src = build_cfg_config(token['code'])
        _img = create_image_from_config(_src, format='png')
        tuples.append(
            (f'{token["type"].upper()}_{token["name"]}', _pseudo, _img, _src))
    return tuples

def change_keys_colors(
        input: str | None = None,
        default: str | None = None,
        If: str | None = None,
        For: str | None = None,
        While: str | None = None,
        Call: str | None = None,
        Return: str | None = None,
        Try: str | None = None,
        Raise: str | None = None,
):
    """change colors of generated images"""
    if isinstance(input, str):
        node_styles['input'] = (node_styles['input'][0], input)
    if isinstance(default, str):
        node_styles['default'] = (node_styles['default'][0], default)
    if isinstance(If, str):
        node_styles[ast.If] = (node_styles[ast.If][0], If)
    if isinstance(For, str):
        node_styles[ast.For] = (node_styles[ast.For][0], For)
    if isinstance(While, str):
        node_styles[ast.While] = (node_styles[ast.While][0], While)
    if isinstance(Call, str):
        node_styles[ast.Call] = (node_styles[ast.Call][0], Call)
    if isinstance(Return, str):
        node_styles[ast.Return] = (node_styles[ast.Return][0], Return)
    if isinstance(Try, str):
        node_styles[ast.Try] = (node_styles[ast.Try][0], Try)
    if isinstance(Raise, str):
        node_styles[ast.Raise] = (node_styles[ast.Raise][0], Raise)
    CFGBuilder.set_styles(node_styles=node_styles)
    
