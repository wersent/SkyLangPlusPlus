from src.lexer.lexer import SkyLexer
from src.parser.parser import SkyParser
from src.interpreter.interpreter import SkyInterpreter
from graphviz import Digraph

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
interpreter.interpret(ast)
