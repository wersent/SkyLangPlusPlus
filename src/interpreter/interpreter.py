class SkyInterpreter:


    def __init__(self):
        self.environment = {}  # Словарь для хранения переменных: {'x': 10, 'y': 20}

    def interpret(self, ast):
        for node in ast:
            self.execute(node)

    def execute(self, node):
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
        else:
            raise RuntimeError(f"Неизвестный узел AST: {node[0]}")

    def isString(self ,val):
        if val[0] == '\"' and val[-1] == '\"':
            return True
        else:
            return False

    def evaluate(self, expr):
        if isinstance(expr, tuple):
            op, val1, val2 = expr

            val1_ev = self.evaluate(val1)
            val2_ev = self.evaluate(val2)

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
        _, name, val = node

        if (name in self.environment):
            self.environment[name] = self.evaluate(val)
        else:
            raise RuntimeError(f"Переменная {name} не объявлена")

    def visit_if(self, node):
        _, condition, body = node

        if self.evaluate(condition):
            for statement in body:
                self.execute(statement)

    def visit_while(self, node):
        _, condition, body = node

        while( self.evaluate(condition) ):
            for statement in body:
                self.execute(statement)

    def visit_io(self, node):
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
