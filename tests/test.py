from src.lexer.lexer import SkyLexer
from src.parser.parser import SkyParser
from src.interpreter.interpreter import SkyInterpreter

def test_parser():
    lexer = SkyLexer()
    parser = SkyParser()
    interpreter = SkyInterpreter()

   # try:
        # Тест 1: Объявление переменной
    code = """
    v x;
    """
    interpreter.interpret(parser.parse(code))
    assert 'x' in interpreter.environment, "Тест 1 не пройден: переменная x не объявлена"

    interpreter.environment.clear()

    # Тест 2: Присваивание значения переменной
    code = """
    v x;
    x = 10;
    """
    interpreter.interpret(parser.parse(code))
    assert interpreter.environment['x'] == 10, "Тест 2 не пройден: переменная x не равна 10"

    interpreter.environment.clear()

    # Тест 3: Арифметические операции
    code = """
    v x;
    x = 5 + 5;
    """
    interpreter.interpret(parser.parse(code))
    assert interpreter.environment['x'] == 10, "Тест 3 не пройден: 5 + 5 != 10"

    interpreter.environment.clear()

    # Тест 4: Условный оператор (if)
    code = """
    v x;
    x = 10;
    if (x > 5) {
        x = 20;
    }
    """
    interpreter.interpret(parser.parse(code))
    assert interpreter.environment['x'] == 20, "Тест 4 не пройден: if не сработал"

    interpreter.environment.clear()

    # Тест 5: Цикл (while)
    code = """
    v x;
    x = 0;
    w (x < 5) {
        x = x + 1;
    }
    """
    interpreter.interpret(parser.parse(code))
    assert interpreter.environment['x'] == 5, "Тест 5 не пройден: while не сработал"

    interpreter.environment.clear()

    # Тест 6: Ввод/вывод (имитация ввода)
    code = """
    v x;
    in(x);
    wrn(x);
    """
    interpreter.interpret(parser.parse(code))
    assert interpreter.environment['x'] == "42", "Тест 6 не пройден: ввод не сработал"

    interpreter.environment.clear()

    # Тест 7: Ввод числа (inn)
    code = """
    v x;
    inn(x);
    wrn(x);
    """

    interpreter.interpret(parser.parse(code))
    assert interpreter.environment['x'] == 42, "Тест 7 не пройден: ввод числа не сработал"

    interpreter.environment.clear()

    # Тест 8: Логические операции
    code = """
    v x;
    x = (5 > 3) & (2 < 4);
    """
    interpreter.interpret(parser.parse(code))
    assert interpreter.environment['x'] == True, "Тест 8 не пройден: логическая операция не сработала"

    interpreter.environment.clear()

    print("Все тесты пройдены успешно!")

    #except RuntimeError:
        #print(1)


# Запуск тестов
test_parser()