from src.lexer.lexer import SkyLexer
from src.parser.parser import SkyParser
from src.interpreter.interpreter import SkyInterpreter

def test_parser():
    lexer = SkyLexer()
    parser = SkyParser()
    interpreter = SkyInterpreter()

    code = '''
    v x;
    inn(x);
    v y = x - 30;
    if ((x > y) | 30 <= 1){
        wrn(x);
        wr(y);
    }
    '''

    ast = parser.parse(code)
    interpreter.interpret(ast)

# Запуск тестов
test_parser()