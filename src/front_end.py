# -*- coding: utf-8 -*-
"""INE 5421 - Linguagem Formais e Compiladores - Trabalho 01

Universidade Federal de Santa Catarina

Departamento de Informática e Estatística (INE)

Alunos:

- Filipe Oliveira de Borba
- Lucas João Martins
"""

from .lexer import Lexer, TokenType
from .parser import Parser


class FrontEnd:

    def __init__(self, source_code_filename, glc_filename):
        self.lexer = Lexer(source_code_filename)
        self.parser = Parser(glc_filename, False)

    def compile_by_phase(self):
        # lexical analysis
        tokens = []
        while True:
            token = self.lexer.next_token()

            # discard and get next one if token is invalid
            while True:
                if token is not None:
                    break
                token = self.lexer.next_token()

            value = token.type.value
            if token.type == TokenType.EOF:
                value = token.lexeme

            tokens.append(value)

            if token.type == TokenType.EOF:
                break

        # prints to just know what is happening

        print(80 * '-' + '\n')

        print('First sets:')
        for key, value in self.parser.first_sets.items():
            print(key, value)
        print(80 * '-' + '\n')

        print('Follow sets:')
        for key, value in self.parser.follow_sets.items():
            print(key, value)
        print(80 * '-' + '\n')

        print('Parsing table:')
        for key, value in self.parser.parsing_table.items():
            print(key, value)
        print(80 * '-' + '\n')

        # syntax analysis
        print('Sequência da execução:')
        if self.parser.parse_by_phase(tokens):
            print(80 * '-' + '\n')
            print('Análise sintática realizada com sucesso :D')
            print(80 * '-' + '\n')
        else:
            print(80 * '-' + '\n')
            print('Erro na análise sintática :(')
            print(80 * '-' + '\n')

    def compile(self):
        print('First sets:')
        for key, value in self.parser.first_sets.items():
            print(key, value)
        print(80 * '-' + '\n')

        print('Follow sets:')
        for key, value in self.parser.follow_sets.items():
            print(key, value)
        print(80 * '-' + '\n')

        print('Parsing table:')
        for key, value in self.parser.parsing_table.items():
            print(key, value)
        print(80 * '-' + '\n')

        while True:
            alright = 0
            token = self.lexer.next_token()

            # discard and get next one if token is invalid
            while True:
                if token is not None:
                    break
                token = self.lexer.next_token()

            while alright == 0:
                alright = self.parser.parse_by_token(token)

            if token.type == TokenType.EOF:
                break

        if alright == 2:
            print(80 * '-' + '\n')
            print('Análise sintática realizada com sucesso :D')
            print(80 * '-' + '\n')
        else:
            print(80 * '-' + '\n')
            print('Erro na análise sintática :(')
            print(80 * '-' + '\n')
