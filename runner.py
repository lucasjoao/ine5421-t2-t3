from lexer import lexer

filename = 'data/tokens'

lex = lexer.Lexer(filename)

tokens = [lex.next_token() for i in range(5)]
print(tokens[0].type == lexer.TokenType.ID)
print(tokens[1].type == lexer.TokenType.WHILE)
print(tokens[2].type == lexer.TokenType.SEMICOLON)
print(tokens[3].type == lexer.TokenType.NUM)
print(tokens[4].type == lexer.TokenType.REAL)

try:
    lex.next_token()
except:
    pass

print(lex.next_token().type == lexer.TokenType.EOF)
