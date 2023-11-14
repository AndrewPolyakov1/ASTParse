import graphviz as gv

if __name__ == '__main__':
    dot = gv.Digraph(comment='The Round Table')

    dot.node('A', 'King Arthur')  # doctest: +NO_EXE
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')
    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='false')

    print(dot.source)

    dot.render('a.gv').replace('\\', '/')