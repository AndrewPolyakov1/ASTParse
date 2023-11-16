import graphviz as gv
from .pseudo import parse, unparse
from .tokenize import tokenize
from .py2cfg_ext import CFGBuilder, CFG
from PIL import Image
import io
import ast

node_styles = CFG.node_styles



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


def build_cfg_config(code: str, pseudocode: bool = True) -> str:
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
    cfg = CFGBuilder(pseudocode=pseudocode).build_from_src('', code)
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



def code_to_image_and_pseudocode(filepath: str, pseudocode: bool = False, format: str = 'png'):
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
        _src = build_cfg_config(token['code'], pseudocode=pseudocode)
        _img = create_image_from_config(_src, format='png')
        tuples.append(
            (f'{token["type"].upper()}_' + f'{token["name"]}', _pseudo, _img, _src))
    # print([i[0] for i in tuples])
    return tuples

def change_keys_colors(
        new_node_colors : dict,
        # input: str | None = None,
        # default: str | None = None,
        # If: str | None = None,
        # For: str | None = None,
        # While: str | None = None,
        # Call: str | None = None,
        # Return: str | None = None,
        # Try: str | None = None,
        # Raise: str | None = None,
):
    """change colors of generated images"""
    # if isinstance(input, str):
    node_styles['input'] = (node_styles['input'][0], new_node_colors['input'])
    # if isinstance(default, str):
    node_styles['default'] = (node_styles['default'][0], new_node_colors['default'])
    # if isinstance(If, str):
    node_styles[ast.If] = (node_styles[ast.If][0], new_node_colors['If'])
    # if isinstance(For, str):
    node_styles[ast.For] = (node_styles[ast.For][0], new_node_colors['For'])
    # if isinstance(While, str):
    node_styles[ast.While] = (node_styles[ast.While][0], new_node_colors['While'])
    # if isinstance(Call, str):
    node_styles[ast.Call] = (node_styles[ast.Call][0], new_node_colors['Call'])
    # if isinstance(Return, str):
    node_styles[ast.Return] = (node_styles[ast.Return][0], new_node_colors['Return'])
    # if isinstance(Try, str):
    node_styles[ast.Try] = (node_styles[ast.Try][0], new_node_colors['Try'])
    # if isinstance(Raise, str):
    node_styles[ast.Raise] = (node_styles[ast.Raise][0], new_node_colors['Raise'])
    CFGBuilder.set_styles(node_styles=node_styles)
    
def get_keys_colors():
    return {
        "input": node_styles['input'][1],
        "default": node_styles['default'][1],  
        "If": node_styles[ast.If][1],  
        "For": node_styles[ast.For][1],  
        "While": node_styles[ast.While][1],  
        "Call": node_styles[ast.Call][1],  
        "Return": node_styles[ast.Return][1],  
        "Try": node_styles[ast.Try][1],
        "Raise": node_styles[ast.Raise][1],
    }
def get_keys_image():
    return Image.open(io.BytesIO(CFGBuilder.get_key_graph_bytes()))

def get_supported_formats():
    formats=['png', 'svg', 'jpg']
    return formats