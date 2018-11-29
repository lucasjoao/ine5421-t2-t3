import copy
from .grammar import Grammar
from .utils import Utils


class Parser:

    def __init__(self, filename, test_env):
        self.glc = Grammar.read_from_json(filename, test_env)
        # make self.first_sets where the key is a NT and the value a set
        self._make_dict_first_sets()
        # make self.follow_sets where the key is a NT and the value a set
        self._make_dict_follow_sets()
        # parsing table where the key is a tuple of (NT, T) and the value is the value in table
        self._make_parsing_table()

    def _make_dict_first_sets(self):
        self.first_sets = {key: set() for key in self.glc._nonterminals}

        while True:
            bckp_first_sets = copy.deepcopy(self.first_sets)
            glc_productions = copy.deepcopy(self.glc._productions)

            for production in glc_productions:
                key = production.pop(0)

                if Utils.EPSILON in production:
                    self.first_sets[key].add(Utils.EPSILON)
                    continue

                self._make_first_set(production, key, True)

            if bckp_first_sets == self.first_sets:
                break

    def _make_first_set(self, production, key, can_add_epsilon):
        symbol = production[0]
        if symbol in self.glc._terminals:
            self.first_sets[key].add(symbol)
        elif symbol in self.glc._nonterminals:
            other_first_set = copy.deepcopy(self.first_sets[symbol])

            if Utils.EPSILON in other_first_set:
                other_first_set.remove(Utils.EPSILON)
                can_add_epsilon = can_add_epsilon and True
                production.remove(symbol)

                # last symbol from a sequence of NT where each one has &
                if not production and can_add_epsilon:
                    self.first_sets[key].add(Utils.EPSILON)
                else:
                    self._make_first_set(production, key, can_add_epsilon)

            self.first_sets[key] = self.first_sets[key].union(other_first_set)

    def _make_dict_follow_sets(self):
        self.follow_sets = {key: set() for key in self.glc._nonterminals}

        self.follow_sets[self.glc._initial_symbol].add(Utils.END_MARK)

        while True:
            bckp_follow_sets = copy.deepcopy(self.follow_sets)

            for key in self.glc._nonterminals:
                glc_productions = copy.deepcopy(self.glc._productions)

                for production in glc_productions:
                    origin_prod = production[0]

                    for symbol in production[1:]:
                        production.remove(symbol)

                        if key == symbol:
                            self._make_follow_set(production[1:], key,
                                                  origin_prod)

            if bckp_follow_sets == self.follow_sets:
                break

    def _make_follow_set(self, production, key, origin_prod):
        if not production:
            self.follow_sets[key] = self.follow_sets[key].union(
                                    self.follow_sets[origin_prod])
        else:
            symbol = production[0]
            if symbol in self.glc._nonterminals:
                first_set = copy.deepcopy(self.first_sets[symbol])

                if Utils.EPSILON in first_set:
                    first_set.remove(Utils.EPSILON)
                    production.remove(symbol)
                    self._make_follow_set(production, key, origin_prod)

                self.follow_sets[key] = self.follow_sets[key].union(first_set)
            elif symbol in self.glc._terminals:
                self.follow_sets[key].add(symbol)

    def _make_parsing_table(self):
        self.parsing_table = {}

        for production in self.glc._productions:
            first = production[1]
            first_set = set()

            if first in self.glc._terminals or first == Utils.EPSILON:
                first_set.add(first)
            else:
                first_set = self.first_sets[first]

            if Utils.EPSILON in first_set:
                for symbol in self.follow_sets[production[0]]:
                    self._add_in_parsing_table(production, symbol)
            else:
                for symbol in first_set:
                    self._add_in_parsing_table(production, symbol)

    def _add_in_parsing_table(self, production, symbol):
        self.parsing_table[production[0], symbol] = production[1:]

    def parse(self, user_input):
        user_input += Utils.END_MARK

        stack = [Utils.END_MARK, self.glc._initial_symbol]
        buffer_index = 0

        while True:
            print(stack)

            stack_top = stack[len(stack) - 1]
            char_input = user_input[buffer_index]

            stack.pop()

            if stack_top == char_input:
                if stack_top == Utils.END_MARK:
                    return True

                buffer_index += 1
            else:
                key = (stack_top, char_input)

                try:
                    value = self.parsing_table[key]
                except KeyError:
                    print('O par ' + str(key) + ' gera erro na parsing table.')
                    return False

                if Utils.EPSILON not in value:
                    for symbol in value[::-1]:
                        stack.append(symbol)
