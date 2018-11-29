from .lexer import Lexer, TokenType
from .parser import Parser


class FrontEnd:

    def __init__(self, source_code_filename, glc_filename):
        self.lexer = Lexer(source_code_filename)
        self.parser = Parser(glc_filename, False)

    def compile(self):
        # lexical analysis
        lexemes = []
        while True:
            token = self.lexer.next_token()

            # discard and get next one if token is invalid
            while True:
                if token is not None:
                    break
                token = self.lexer.next_token()

            lexemes.append(token.lexeme)

            if token.type == TokenType.EOF:
                break

        # syntax analysis
        if self.parser.parse(lexemes):
            print('Análise sintática realizada com sucesso :D')
        else:
            print('Erro na análise sintática :(')

