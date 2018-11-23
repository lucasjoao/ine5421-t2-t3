from lexer import lexer

filename = 'data/tokens'

lex = lexer.Lexer(filename)

tokens = [lex.next_token() for i in range(6)]

print('Lexema ' + tokens[0].lexeme + ' é do tipo ID?')
print(tokens[0].type == lexer.TokenType.ID)

print('Lexema ' + 'while' + ' é do tipo WHILE?')  # FIXME: check this problem
print(tokens[1].type == lexer.TokenType.WHILE)

print('Lexema ' + ';' + ' é do tipo SEMICOLON?')  # FIXME: check this problem
print(tokens[2].type == lexer.TokenType.SEMICOLON)

print('Lexema ' + tokens[3].lexeme + ' é do tipo NUM?')
print(tokens[3].type == lexer.TokenType.NUM)

print('Lexema ' + tokens[4].lexeme + ' é do tipo REAL?')
print(tokens[4].type == lexer.TokenType.REAL)

print('Lexema ' + 'if' + ' é do tipo IF?')  # FIXME: check this problem
print(tokens[5].type == lexer.TokenType.IF)

try:
    lex.next_token()
except:
    pass

print('Chegou no fim do arquivo?')
print(lex.next_token().type == lexer.TokenType.EOF)

print('Testando source.c')
lex = lexer.Lexer('data/source.c')
t = lex.next_token()
while t.type != lexer.TokenType.EOF:
    print(t.type.name)
    t = lex.next_token()
print('Leitura bem sucedida!')
