# -*- coding: utf-8 -*-
"""INE 5421 - Linguagem Formais e Compiladores - Trabalho 01

Universidade Federal de Santa Catarina

Departamento de Informática e Estatística (INE)

Alunos:

- Filipe Oliveira de Borba
- Lucas João Martins
"""

import enum
from .utils import Utils


class TokenType(enum.Enum):
    LEFT_PAR = '('
    RIGHT_PAR = ')'
    MULTIPLICATION = '*'
    PLUS = '+'
    MINUS = '-'
    DIVISION = '/'
    SEMICOLON = ';'
    LEFT_CURLY = '{'
    RIGHT_CURLY = '}'
    ASSIGNMENT = '='
    LEFT_SQUARE = '['
    RIGHT_SQUARE = ']'

    EOF = 256
    IF = 'if'
    THEN = 'then'
    ELSE = 'else'
    WHILE = 'while'
    DO = 'do'
    BREAK = 'break'
    TRUE = 'true'
    FALSE = 'false'
    ID = 'id'
    NUM = 'num'
    REAL = 'real'
    RELOP = 'relop'
    BASIC = 'basic'


class Token(object):

    def __init__(self, type, lexeme=None):
        self.type = type
        self.lexeme = lexeme


class Lexer(object):

    def __init__(self, filename):
        self._source = open(filename, 'r')
        self._eof = self._source.seek(0, 2)
        self._source.seek(0)
        self._ln_number = 1
        self._col_number = 0

    def next_token(self):
        self._skip_space()
        lookahead = self._next_char()
        if not lookahead:
            return Token(TokenType.EOF, Utils.END_MARK)
        if lookahead.isdigit():
            self._retract()
            return self._next_num_or_real()
        if lookahead.isalpha():
            self._retract()
            return self._next_word()
        if lookahead in '=<>!':
            self._retract()
            return self._next_relop()
        try:
            return Token(TokenType(lookahead), lookahead)
        except ValueError:
            print('Caracter ' + lookahead + ' inválido na ' +
                  'linha ' + str(self._ln_number) + ' ' +
                  'e coluna ' + str(self._col_number))

    def _next_num_or_real(self):
        lexeme = self._read_digits()
        if self._next_char() != '.':
            self._retract()
            return Token(TokenType.NUM, lexeme)
        fraction = self._read_digits()
        if not fraction:
            raise Exception('missing digits after dot')
        lexeme += '.' + fraction
        return Token(TokenType.REAL, lexeme)

    def _read_digits(self):
        lexeme = ''
        lookahead = self._next_char()
        while lookahead.isdigit():
            lexeme += lookahead
            lookahead = self._next_char()
        self._retract()
        return lexeme

    def _next_word(self):
        lexeme = ''
        lookahead = self._next_char()
        while lookahead.isalpha() or (lookahead == '_'):
            lexeme += lookahead
            lookahead = self._next_char()
        self._retract()
        if lexeme in RESERVED_WORDS:
            return Token(RESERVED_WORDS[lexeme], lexeme)
        return Token(TokenType.ID, lexeme)

    def _next_relop(self):
        lexeme = self._next_char()
        lookahead = self._next_char()
        if lookahead == '=':
            lexeme += lookahead
            return Token(TokenType.RELOP, lexeme)
        self._retract()
        if lexeme == '=':
            return Token(TokenType.ASSIGNMENT, lexeme)
        return Token(TokenType.RELOP, lexeme)

    def _next_char(self):
        self._col_number += 1
        return self._source.read(1)

    def _retract(self):
        self._col_number -= 1
        current_pos = self._source.tell()
        if current_pos != self._eof:
            self._source.seek(current_pos - 1)

    def _skip_space(self):
        ch = self._next_char()
        while ch.isspace():
            if ch == '\n':
                self._col_number = 0
                self._ln_number += 1
            ch = self._next_char()
        if ch:
            self._retract()


RESERVED_WORDS = {
    'if': TokenType.IF,
    'then': TokenType.THEN,
    'else': TokenType.ELSE,
    'while': TokenType.WHILE,
    'do': TokenType.DO,
    'break': TokenType.BREAK,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'int': TokenType.BASIC,
    'float': TokenType.BASIC
}
