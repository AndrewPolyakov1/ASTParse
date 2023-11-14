import my_ast

python_file = 'ex_class.py'


def main():
    with open("ex_class.py", "r") as file:
        code = file.read()

    tree = my_ast.parse(code)
    # print (my_ast.dump(tree, indent=4))
    
    unparsed_code = my_ast.unparse(tree)
    # print(unparsed_code)

    with open("ex_class.py" + '_pseudo.txt', 'w') as file_res:
        file_res.write(unparsed_code)

if __name__ == '__main__':
    main()