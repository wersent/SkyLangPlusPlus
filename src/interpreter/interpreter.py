"""
Модуль интерпретатора для языка SkyLang/ScyScraper.

Осуществляет выполнение абстрактного синтаксического дерева (AST)
с использованием visitor-паттерна. Управляет состоянием среды выполнения,
обрабатывает переменные и выполняет базовые операции ввода-вывода.
"""

class SkyInterpreter:
    """
        Основной класс интерпретатора SkyLang.

        :attr environment: Словарь для хранения переменных и их значений
        """

    def __init__(self):
        """
                Инициализация интерпретатора.
                Создает пустое окружение для хранения переменных.
                """
        self.environment = {}  # Словарь для хранения переменных: {'x': 10, 'y': 20}
        self.classes = {}  # Классы
        self.objects = {}  # Объекты (экземпляры)

    def interpret(self, ast):
        """
                Основной метод для запуска интерпретации AST.

                :param ast: Абстрактное синтаксическое дерево программы
                :type ast: list
                :raises RuntimeError: При обнаружении неизвестного узла AST
                """
        for node in ast:
            self.execute(node)

    def execute(self, node):
        """
                Диспетчер выполнения узлов AST. Определяет тип узла и вызывает
                соответствующий метод-обработчик.

                :param node: Узел AST для выполнения
                :raises RuntimeError: Для неизвестных типов узлов
                """

        # Определяем тип узла и вызываем соответствующий метод
        if node[0] == 'declare':
            self.visit_declare(node)
        elif node[0] == 'assign':
            self.visit_assign(node)
        elif node[0] == 'if':
            self.visit_if(node)
        elif node[0] == 'while':
            self.visit_while(node)
        elif node[0] == 'io':
            self.visit_io(node)
        elif node[0] == 'class':
            self.visit_class(node)
        elif node[0] == 'new':
            self.visit_new(node)
        elif node[0] == 'get_member':
            return self.visit_get_member(node)
        elif node[0] == 'call_method':
            return self.visit_call_method(node)
        else:
            raise RuntimeError(f"Неизвестный узел AST: {node[0]}")

    def isString(self, val):
        """
                Проверяет, является ли значение строковым литералом.

                :param val: Проверяемое значение
                :return: True если значение в двойных кавычках
                :rtype: bool
                """

        if val[0] == '\"' and val[-1] == '\"':
            return True
        else:
            return False

    def evaluate(self, expr):
        """
                Рекурсивно вычисляет значение выражения.

                Поддерживаемые операции:
                - Арифметические: +, -, *, /
                - Сравнения: >, <, >=, <=, ==
                - Логические: & (and), | (or)
                - Унарное отрицание: !
                - Работа с переменными и литералами

                :param expr: Выражение для вычисления
                :return: Результат вычисления (int, str, bool)
                :rtype: mixed
                :raises RuntimeError: При ошибках типов или неопределенных переменных
                """

        if isinstance(expr, tuple):
            op, val1, val2 = expr

            val1_ev = self.evaluate(val1)
            val2_ev = self.evaluate(val2)

            if isinstance(val1_ev, float):
                val1_ev = int(val1_ev)
            if isinstance(val2_ev, float):
                val1_ev = int(val2_ev)

            match (op):
                case '+':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int): # int int
                        return val1_ev + val2_ev
                    elif isinstance(val1_ev, str) and isinstance(val2_ev, int): # str int
                        return val1_ev + str(val2_ev)
                    elif isinstance(val1_ev, int) and isinstance(val2_ev, str): # int str
                        return str(val1_ev) + val2_ev
                    else:
                        raise RuntimeError(f"Незвестная ошибка при сложении {val1_ev} и {val2_ev}")

                case '-':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int): # int int
                        return val1_ev - val2_ev
                    else:
                        raise RuntimeError(f"Невозможно вычесть {type(val1_ev)} и {type(val2_ev)}")

                case '*':
                        if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                            return val1_ev * val2_ev
                        else:
                            raise RuntimeError(f"Невозможно умножить {type(val1_ev)} и {type(val2_ev)}")

                case '/':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev / val2_ev
                    else:
                        raise RuntimeError(f"Невозможно разделить {type(val1_ev)} и {type(val2_ev)}")

                case '>':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev > val2_ev
                    else:
                        raise RuntimeError(f"Невозможно сравнить {type(val1_ev)} и {type(val2_ev)}")

                case '<':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev < val2_ev
                    else:
                        raise RuntimeError(f"Невозможно сравнить {type(val1_ev)} и {type(val2_ev)}")

                case '>=':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev >= val2_ev
                    else:
                        raise RuntimeError(f"Невозможно сравнить {type(val1_ev)} и {type(val2_ev)}")

                case '<=':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev <= val2_ev
                    else:
                        raise RuntimeError(f"Невозможно сравнить {type(val1_ev)} и {type(val2_ev)}")

                case '==':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev == val2_ev
                    else:
                        raise RuntimeError(f"Невозможно сравнить {type(val1_ev)} и {type(val2_ev)}")

                case '&':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev and val2_ev
                    else:
                        raise RuntimeError(f"Невозможно сравнить {type(val1_ev)} и {type(val2_ev)}")

                case '|':
                    if isinstance(val1_ev, int) and isinstance(val2_ev, int):  # int int
                        return val1_ev or val2_ev
                    else:
                        raise RuntimeError(f"Невозможно сравнить {type(val1_ev)} и {type(val2_ev)}")


        elif isinstance(expr, int): # число
            return int(expr)

        elif isinstance(expr, str) and self.isString(expr):  # строка
                return expr[1: -1]

        elif isinstance(expr, str): # переменная
            if expr in self.environment:
                return self.environment[expr]
            else:
                raise RuntimeError(f"Переменная {expr} не определена")

    def visit_declare(self, node):
        """
                Обработка объявления переменных.

                Примеры:
                - var x;       -> (declare, 'x')
                - var x = 10;  -> (declare, 'x', 10)

                :param node: Узел объявления
                :raises RuntimeError: При повторном объявлении
                """

        if len(node) == 2:
            _, name = node
        else:
            _, name, val = node


        if (name in self.environment):
            raise RuntimeError(f"Переменная уже определена")

        if (len(node) == 2):
            self.environment[name] = None
        else:
            self.environment[name] = self.evaluate(val)

    def visit_assign(self, node):
        """
                Обработка операции присваивания значения переменной.

                Пример:
                - x = 10;  -> (assign, 'x', 10)

                :param node: Узел присваивания
                :raises RuntimeError: Если переменная не была объявлена
                """

        _, name, val = node

        if (name in self.environment):
            self.environment[name] = self.evaluate(val)
        else:
            raise RuntimeError(f"Переменная {name} не объявлена")

    def visit_if(self, node):
        """
                Обработка условного оператора if.

                Пример:
                - if (x > 10) { ... }  -> (if, условие, тело)

                :param node: Узел условного оператора
                """

        _, condition, body = node

        if self.evaluate(condition):
            for statement in body:
                self.execute(statement)

    def visit_while(self, node):
        """
                Обработка цикла while.

                Пример:
                - while (x < 10) { ... }  -> (while, условие, тело)

                :param node: Узел цикла
                """

        _, condition, body = node

        while( self.evaluate(condition) ):
            for statement in body:
                self.execute(statement)

    def visit_io(self, node):
        """
                Обработка операций ввода-вывода.

                Поддерживаемые команды:
                - wr:   вывод без перевода строки
                - wrn:  вывод с переводом строки
                - in:   ввод строки
                - inn:  ввод числа

                :param node: Узел ввода-вывода
                :raises RuntimeError: При работе с необъявленными переменными
                """

        _, command, var = node

        match(command):
            case 'wr':
                print(self.evaluate(var), end="")
            case 'wrn':
                print(self.evaluate(var))
            case 'in':
                tmp = input()
                if (var in self.environment):
                    self.environment[var] = tmp
                else:
                    raise RuntimeError(f"Переменная {var} не объявлена")
            case 'inn':
                tmp = input()
                if tmp.isdigit():
                    tmp = int(tmp)
                    if (var in self.environment):
                        self.environment[var] = tmp
                    else:
                        raise RuntimeError(f"Переменная {var} не объявлена")

    def visit_class(self, node):
        """
        Сохраняет определение класса в словаре self.classes.
        :param node: ('class', 'Person', [body])
        """
        _, class_name, body = node

        # Извлекаем поля и методы
        fields = []
        methods = {}

        for member in body:
            _, access, decl_node = member

            if decl_node[0] == 'declare':
                var_name = decl_node[1]
                fields.append(var_name)

            elif decl_node[0] == 'function':
                func_name = decl_node[2]
                methods[func_name] = decl_node

        self.classes[class_name] = {
            'fields': fields,
            'methods': methods
        }

    def visit_new(self, node):
        """
        Создаёт экземпляр класса.
        Пример: ('new', 'Person')
        :param node: ('new', 'Person')
        """
        _, class_name = node
        if class_name not in self.classes:
            raise RuntimeError(f"Класс {class_name} не найден")

        # Создаём "объект" как словарь
        obj = {
            'class': class_name,
            'fields': {}
        }

        return obj

    def visit_get_member(self, node):
        """
        Получает значение поля объекта.
        Пример: ('get_member', 'p', 'name')
        """
        _, obj_expr, field_name = node

        obj = self.evaluate(obj_expr)
        if not isinstance(obj, dict) or 'class' not in obj:
            raise RuntimeError(f"{obj_expr} не является объектом")

        class_name = obj['class']
        class_def = self.classes.get(class_name)

        # Проверяем, есть ли такое поле в полях класса
        if field_name not in class_def['fields']:
            raise RuntimeError(f"Поле {field_name} отсутствует в классе {class_name}")

        return obj['fields'].get(field_name)

    def visit_call_method(self, node):
        """
        Вызывает метод объекта.
        Пример: ('call_method', 'p', 'SetName', ['Alice'])
        """
        _, obj_expr, method_name, args = node

        obj = self.evaluate(obj_expr)
        if not isinstance(obj, dict) or 'class' not in obj:
            raise RuntimeError(f"{obj_expr} не является объектом")

        class_name = obj['class']
        class_def = self.classes.get(class_name)

        if method_name not in class_def['methods']:
            raise RuntimeError(f"Метод {method_name} не определён в классе {class_name}")

        method_node = class_def['methods'][method_name]

        # Здесь можно передавать аргументы внутрь функции
        # Например, формируем новое окружение внутри метода
        _, return_type, method_name, parameters, body = method_node

        # Сохраняем текущее состояние
        old_env = self.environment.copy()

        # Предположим, что параметры — это список ('args', 'n'), например
        # Нужно привести их к виду {'param': value}
        # Но здесь нужно больше деталей из твоего парсера

        # Для примера просто объявляем 'this' и передаём аргументы
        this = obj

        # Сохраняем this и параметры
        self.environment['this'] = this
        for i, param in enumerate(parameters):
            self.environment[param] = self.evaluate(args[i])

        # Выполняем тело метода
        for stmt in body:
            self.execute(stmt)

        # Восстанавливаем старое окружение
        self.environment.clear()
        self.environment.update(old_env)

