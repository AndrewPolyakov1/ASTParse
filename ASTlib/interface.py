import graphviz as gv
from .pseudo import parse, unparse


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

def translate(code: str) -> str:
    tree = parse(code)    
    unparsed_code = unparse(tree)
    return unparsed_code


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
        l = translate(f.read())
        print(l)
