from src.lexer.lexer import SkyLexer
from src.parser.parser import SkyParser
from src.interpreter.interpreter import SkyInterpreter
from graphviz import Digraph

lexer = SkyLexer()
parser = SkyParser()
interpreter = SkyInterpreter()

code = '''
c Person{
    p v name;
    pr int age;

    p void SetName(string nam){
        name = nam;
    }
}

Person per = n Person();
per.SetName("penis");
'''

ast = parser.parse(code)
interpreter.interpret(ast)
