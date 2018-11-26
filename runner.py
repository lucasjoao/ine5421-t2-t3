from src import lexer, grammar

filename = 'data/tokens'

lex = lexer.Lexer(filename)

tokens = [lex.next_token() for i in range(6)]

print('Lexema ' + tokens[0].lexeme + ' é do tipo ID?')
print(tokens[0].type == lexer.TokenType.ID)

print('Lexema ' + tokens[1].lexeme + ' é do tipo WHILE?')
print(tokens[1].type == lexer.TokenType.WHILE)

print('Lexema ' + tokens[2].lexeme + ' é do tipo SEMICOLON?')
print(tokens[2].type == lexer.TokenType.SEMICOLON)

print('Lexema ' + tokens[3].lexeme + ' é do tipo NUM?')
print(tokens[3].type == lexer.TokenType.NUM)

print('Lexema ' + tokens[4].lexeme + ' é do tipo REAL?')
print(tokens[4].type == lexer.TokenType.REAL)

print('Lexema ' + tokens[5].lexeme + ' é do tipo IF?')
print(tokens[5].type == lexer.TokenType.IF)

try:
    lex.next_token()
except:
    pass

print('Chegou no fim do arquivo?')
print(lex.next_token().type == lexer.TokenType.EOF)

# source.c cannot has an error at first position
print('Testando source.c')
lex = lexer.Lexer('data/source.c')
t = lex.next_token()

while t.type != lexer.TokenType.EOF:
    print(t.type.name)
    t = lex.next_token()

    # discard and get next one if token is invalid
    while True:
        if t is not None:
            break
        t = lex.next_token()
print('Leitura finalizada!')

print('GLC em memória')
glc = grammar.Grammar.read_from_json('data/glc', False)
print('não-terminais:')
print(len(glc._nonterminals))
print(glc._nonterminals)
print('terminais:')
print(len(glc._terminals))
print(glc._terminals)
print('Fim da verificação da GLC em memória')

