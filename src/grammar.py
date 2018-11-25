import json
from .lexer import TokenType
from .utils import Utils


class Grammar:

    def __init__(self, productions, initial_symbol):
        """Constructs a grammar from a list of productions and the initial symbol.

        Assumes each production "A -> aB", where B is optional, is of the form:
            ("A", "a"[, "B"])
        """
        self._initial_symbol = initial_symbol
        self._productions = set(productions)
        self._nonterminals = {self._initial_symbol}
        self._terminals = set()
        self._get_nonterminals_and_terminals()

    def save_json(self, filename):
        data = {
            'nonterminals': self._nonterminals,
            'terminals': self._terminals,
            'productions': self._productions,
            'initial_symbol': self._initial_symbol
        }
        with open(filename + '.json', 'w') as write_file:
            json.dump(data, write_file, indent=4)

    def _get_nonterminals_and_terminals(self):
        for production in self._productions:
            for symbol in production:
                if symbol != Utils.EPSILON:
                    # terminals don't have _ in work's glc
                    if not symbol.isalpha() and '_' not in symbol:
                        self._terminals.add(symbol)
                    elif symbol.upper() in TokenType.__members__:
                        self._terminals.add(symbol)
                    else:
                        self._nonterminals.add(symbol)

    @staticmethod
    def read_from_json(filename):
        with open(filename + '.json', 'r') as read_file:
            data = json.load(read_file)
        productions = [tuple(production) for production in data['productions']]
        initial_symbol = data['initial_symbol']
        return Grammar(productions, initial_symbol)
