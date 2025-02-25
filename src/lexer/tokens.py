tokens = {
    # Арифметические
    "NUMBER",
    "PLUS",      # +
    "MINUS",     # -
    "DIV",       # /
    "MULTIPLY",  # *
    "EQ",        # =

    # I/O система
    "IN",
    "INN",
    "WRITE",
    "WRITEN",

    # Сравнение
    "GR",  # >
    "LS",  # <
    "GREQ",  # >=
    "LSEQ",  # <=
    "EQEQ",  # ==

    # Логические
    "AND",  # &
    "OR",  # |
    "NOT",  # !

    "IF",
    "WHILE",

    # Синтаксис
    "BRO",  # (
    "BRC",  # )
    "BLOCKS",  # {
    "BLOCKE",  # }

    "VAR"  # Переменная
    "STRING"
}

keywords = {
    'v': 'VAR',
    'if': 'IF',
    'w': 'WHILE',
    'in': 'IN',
    'inn': 'INN',
    'wr': 'WRITE',
    'wrn': 'WRITEN',
}

t_PLUS = r'\+'
t_MINUS = r'-'
t_DIV = r'/'
t_MULT = r'\*'
t_EQ = r'='
t_AND = r'&'
t_OR = r'\|'
t_NOT = r'!'
t_BRO = r'\('
t_BRC = r'\)'
t_BLOCKS = r'\{'
t_BLOCKE = r'\}'
t_ignore = ' \t'
