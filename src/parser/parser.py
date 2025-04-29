from ply import yacc
from src.lexer.lexer import SkyLexer

class SkyParser:
    """
       Основной класс парсера для построения абстрактного синтаксического дерева (AST).

       :attr lexer: Экземпляр лексера SkyLexer
       :attr tokens: Список токенов (наследуется от лексера)
       :attr parser: Экземпляр PLY-парсера
       :attr precedence: Таблица приоритетов и ассоциативности операторов
       """

    def __init__(self):
        self.lexer = SkyLexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULT', 'DIV'),
        ('nonassoc', 'GR', 'LS', 'GREQ', 'LSEQ', 'EQEQ')
    )

    def p_program(self, p):
        ''' program : statement
                    | program statement
        '''

        if len(p) == 2:
            p[0] = [p[1]]  # Программа из одного statement
        else:
            p[0] = p[1] + [p[2]]  # Добавляем statement к существующей программе

    def p_io(self, p):
        '''io : WRITE BRO expression BRC SEMICOLON
              | WRITEN BRO expression BRC SEMICOLON
              | IN BRO ID BRC SEMICOLON
              | INN BRO ID BRC SEMICOLON
        '''
        p[0] = ('io', p[1], p[3])

    def p_statement(self, p):
        '''
        statement : declaration
                  | condition
                  | cycle
                  | expression SEMICOLON
                  | io
                  | assign
                  | class_declaration
        '''
        p[0] = p[1]

    def p_declaration(self, p):
        '''declaration : VAR ID EQ expression SEMICOLON
                       | VAR ID SEMICOLON
        '''
        if (len(p) == 6):
            p[0] = ('declare', p[2], p[4])
        else:
            p[0] = ('declare', p[2])

    def p_assign(self, p):
        'assign : ID EQ expression SEMICOLON'
        p[0] = ('assign', p[1], p[3])

    def p_expression(self, p):
        '''expression : expression PLUS expression
                      | expression MINUS expression
                      | expression MULT expression
                      | expression DIV expression
                      | expression EQEQ expression
                      | expression GREQ expression
                      | expression LSEQ expression
                      | expression LS expression
                      | expression GR expression
                      | expression AND expression
                      | expression OR expression
                      | NUMBER
                      | ID
                      | STRING
                      | BRO expression BRC
                      | NOT BRO expression BRC
        '''
        if (len(p) == 2):
            p[0] = p[1]
        elif p[1] == '(':
            p[0] = p[2]
        elif p[1] == '!':  # Унарный NOT
            p[0] = ('!', p[3])
        else:
            p[0] = (p[2], p[1], p[3])

    def p_condition(self, p):
        'condition : IF BRO expression BRC BLOCKS program BLOCKE'

        p[0] = ('if', p[3], p[6])

    def p_cycle(self, p):
        'cycle : WHILE BRO expression BRC BLOCKS program BLOCKE'

        p[0] = ('while', p[3], p[6])

    def p_class(self, p):
        '''class_declaration : CLASS ID BLOCKS class_body BLOCKE'''
        p[0] = ('class', p[2], p[4])  # ('class', 'Person', [...])

    def p_class_body(self, p):
        '''class_body :
                      | class_member
                      | class_body class_member
        '''
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_class_member(self, p):
        '''class_member : access_specifier declaration SEMICOLON
                        | access_specifier function SEMICOLON'''
        p[0] = ('member', p[1], p[2])  # ('member', 'public', ('declare', ...))

    def p_access_specifier(self, p):
        '''access_specifier : PUBLIC
                            | PRIVATE
        '''
        p[0] = p[1]

    def p_expression_new(self, p):
        'expression : NEW ID BRO BRC'
        p[0] = ('new', p[2])  # ('new', 'Person')

    def p_expression_dot_access(self, p):
        'expression : expression DOT ID'
        p[0] = ('get_member', p[1], p[3])

    def p_expression_method_call(self, p):
        'expression : expression DOT ID BRO args BRC'
        p[0] = ('call_method', p[1], p[3], p[5])  # ('call_method', 'p', 'setName', ['Alice'])

    def p_args(self, p):
        '''args :
                | expression
                | args COMMA expression'''
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_function(self, p):
        '''function : TYPE ID BRO args BRC BLOCKS program BLOCKE'''
        p[0] = ('function', p[1], p[2], p[4], p[7])

    def p_typed_declaration(self, p):
        'declaration : TYPE ID EQ expression SEMICOLON'
        p[0] = ('declare', p[2], p[1], p[4])  # ('declare', 'name', 'string', '"Alice"')

    def p_error(self, p):
        print(f"Синтаксическая ошибка: {p.value}")

    def parse(self, code):
        return self.parser.parse(code, lexer=self.lexer.lexer)
