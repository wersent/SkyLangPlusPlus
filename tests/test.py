from src.lexer.lexer import SkyLexer

lexer = SkyLexer()
data = 'if x >= 10 { wr("Hello") }'
tokens = lexer.tokenize(data)

for token in tokens:
    print(token)