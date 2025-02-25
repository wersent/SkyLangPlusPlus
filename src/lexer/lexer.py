from ply import lex
from tokens import tokens, keywords


class SkyLexer:
    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Токены:

    def t_NUMBER(t):
        r'\d+'  # регулярное выражение для чисел
        t.value = int(t.value)  # преобразуем строку в число
        return t

    def t_STRING(t):
        r'[^"]*'
        t.value = t.value[1:-1]
        return t

    def t_IN(t):
        r'in'
        t.type = 'IN'
        return t

    def t_INN(t):
        r'inn'
        t.type = 'INN'
        return t

    def t_WRITE(t):
        r'wr'
        t.type = 'WRITE'
        return t

    def t_WRITEN(t):
        r'wrn'
        t.type = 'WRITEN'
        return t

    def t_GREQ(t):
        r'>='
        t.type = 'GREQ'
        return t

    def t_LSEQ(t):
        r'<='
        t.type = 'LSEQ'
        return t

    def t_EQEQ(t):
        r'=='
        t.type = 'EQEQ'
        return t

    def t_IF(t):
        r'if'
        t.type = 'IF'
        return t