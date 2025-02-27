from ply import lex
from .tokens import tokens, keywords


class SkyLexer:
    """
        Основной класс лексера для обработки исходного кода SkyLang.

        :attr tokens: Список имен токенов (наследуется из модуля tokens)
        :attr keywords: Словарь ключевых слов языка (наследуется из модуля tokens)
        :attr lexer: Экземпляр PLY-лексера
        :attr _ignore: Символы, которые следует игнорировать (пробел, таб, новая строка)
        """

    def __init__(self):
        self.tokens = tokens
        self.keywords = keywords
        self.lexer = lex.lex(module=self)

    # Простые токены

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_DIV = r'/'
    t_MULT = r'\*'
    t_EQ = r'='
    t_GR = r'>'
    t_LS = r'<'
    t_AND = r'&'
    t_OR = r'\|'
    t_NOT = r'!'
    t_BRO = r'\('
    t_BRC = r'\)'
    t_BLOCKS = r'\{'
    t_BLOCKE = r'\}'
    t_SEMICOLON = r';'
    t_ignore = ' \t\n'

    # Сложные токены:

    def t_NUMBER(self, t):
        r'\d+'  # регулярное выражение для чисел
        t.value = int(t.value)  # преобразуем строку в число
        return t

    def t_STRING(self, t):
        r'"[^"]*"'
        #t.value = t.value[1:-1]
        return t

    def t_GREQ(self, t):
        r'>='
        t.type = 'GREQ'
        return t

    def t_LSEQ(self, t):
        r'<='
        t.type = 'LSEQ'
        return t

    def t_EQEQ(self, t):
        r'=='
        t.type = 'EQEQ'
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.keywords.get(t.value, 'ID')
        return t

    def t_error(self, t):
        print(f"Неизвестный символ '{t.value[0]}' на позиции {t.lexpos}")
        t.lexer.skip(1)

    def tokenize(self, text):
        """
                Основной метод для токенизации входного текста.

                :param text: Исходный код для обработки
                :type text: str
                :return: Список токенов
                :rtype: list[LexToken]
                """
        self.lexer.input(text)
        return list(self.lexer)

