import graphviz as gv
from .pseudo import parse, unparse
from .tokenize import tokenize
from .py2cfg_ext import CFGBuilder
from PIL import Image
import io


def build_cfg_config(code: str):
    raise NotImplementedError


def build_cfg_config_file(code: str, name: str):
    raise NotImplementedError


def create_image_from_file(path: str, name: str):
    with open(path, 'r') as f:
        source = f.read()
        create_image_from_config(source, name)


def create_image_from_config(config: str, name: str):
    dot = gv.Source(config, format='png')
    dot.render(name).replace('\\', '/')


def wrapper_image(code: str, name: str):
    config = build_cfg_config(code)
    return create_image_from_config(config, name)


def create_image(code: str):  # -> PIL Image
    """
    Get the CFG of the code

    Parameters
    ----------
    filepath : str
        Filename of module to parse.

    Returns
    -------
    Image
        Image of CFG
    """
    cfg = CFGBuilder().build_from_src('', code)
    pic_bytes = cfg.build_visual(
        None,  # f'exampleCFG_{i}',
        'png',
        build_keys=False,
        show=False,
        calls=False,
        includeDefs=False
    )
    return Image.open(io.BytesIO(pic_bytes))


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


def wrapper(filepath: str):
    """
    Returns List of tuples of format
        (name: str, code: str, Image)

    Parameters
    ----------
    filepath : str
        Filename of module to parse.

    Returns
    -------
    tuple
        (name: str, code: str, Image)
    """
    tokens = tokenize(filepath)
    tuples = []
    for token in tokens:
        _pseudo = translate(token['code'])
        _img = create_image(token['code'])
        tuples.append(
            (f'{token["type"].upper()}_{token["name"]}', _pseudo, _img))
    return tuples


if __name__ == "__main__":
    config = '''
    digraph "cluster0.tmp/FUNCTION foo" {
	graph [compound=True fontname="DejaVu Sans Mono" label=".tmp/FUNCTION foo" pack=False rankdir=TB ranksep=0.02]
	node [fontname="DejaVu Sans Mono"]
	edge [fontname="DejaVu Sans Mono"]
	1 [label="def foo(a: int):...\l" fillcolor="#FFFB81" shape=rectangle style="filled,solid"]
	subgraph cluster0foo {
		graph [compound=True fontname="DejaVu Sans Mono" label=foo pack=False rankdir=TB ranksep=0.02]
		node [fontname="DejaVu Sans Mono"]
		edge [fontname="DejaVu Sans Mono"]
		3 [label="return a * 2\l" fillcolor="#98fb98" shape=parallelogram style="filled,solid"]
	}
}
    '''
    with open('pseudo/ex_class.py') as f:
        create_image('tmp/im', f.read())
