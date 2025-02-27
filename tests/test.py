from src.lexer.lexer import SkyLexer
from src.parser.parser import SkyParser
from src.interpreter.interpreter import SkyInterpreter
from graphviz import Digraph


def visualize_ast(ast, output_file='ast'):
    """
    Визуализирует AST с настройками стиля.
    """
    dot = Digraph(comment='AST', format='png')
    dot.attr('node', shape='box', style='filled', color='lightblue', fontname='Arial')
    dot.attr('edge', color='gray50')

    def add_nodes_edges(node, parent_id=None):
        if isinstance(node, (list, tuple)):
            node_id = str(id(node))
            label = node[0] if isinstance(node, tuple) else "program"
            dot.node(node_id, label, fillcolor='lightblue', fontcolor='black')

            if parent_id:
                dot.edge(parent_id, node_id, color='gray50')

            for child in node[1:] if isinstance(node, tuple) else node:
                add_nodes_edges(child, node_id)
        else:
            node_id = str(id(node))
            dot.node(node_id, str(node), fillcolor='lightgreen', fontcolor='black')
            if parent_id:
                dot.edge(parent_id, node_id, color='gray50')

    add_nodes_edges(ast)
    dot.render(output_file, cleanup=True)
    print(f"AST сохранен в {output_file}.png")


lexer = SkyLexer()
parser = SkyParser()
interpreter = SkyInterpreter()

code = '''
v x;
inn(x);
v y = 15;
if ((x > y) | ((x / 2) == 6)){
    wrn(x);
    wr(y);
}
'''

ast = parser.parse(code)

visualize_ast(ast, output_file='ast_tree')
