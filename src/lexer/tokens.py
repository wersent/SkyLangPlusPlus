tokens = (
    # Арифметические
    "NUMBER",
    "PLUS",      # +
    "MINUS",     # -
    "DIV",       # /
    "MULT",  # *
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
    "SEMICOLON",  # ;

    "VAR",  # Переменная
    "STRING",
    "ID",

    "CLASS",
    "PUBLIC",
    "PRIVATE",
    "NEW",
    "DOT",
    "COMMA",
    "TYPE",
)

keywords = {
    'v': 'VAR',
    'if': 'IF',
    'w': 'WHILE',
    'in': 'IN',
    'inn': 'INN',
    'wr': 'WRITE',
    'wrn': 'WRITEN',
    'c': 'CLASS',
    'p': 'PUBLIC',
    'pr': 'PRIVATE',
    'n': 'NEW',
}
