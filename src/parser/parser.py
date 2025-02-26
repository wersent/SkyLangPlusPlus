from ply import yacc
from src.lexer.lexer import SkyLexer

class SkyParser:
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
        '''
        p[0] = p[1]  # Сохраняем результат под-правила

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
        else:
            p[0] = (p[2], p[1], p[3])

    def p_condition(self, p):
        'condition : IF BRO expression BRC BLOCKS program BLOCKE'

        p[0] = ('if', p[3], p[6])

    def p_cycle(self, p):
        'cycle : WHILE BRO expression BRC BLOCKS program BLOCKE'

        p[0] = ('while', p[3], p[6])

    def p_error(self, p):
        print(f"Синтаксическая ошибка: {p.value}")

    def parse(self, code):
        return self.parser.parse(code, lexer=self.lexer.lexer)
