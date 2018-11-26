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
        symbol = copy.deepcopy(production)[0]
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
            glc_productions = copy.deepcopy(self.glc._productions)

            for key in self.glc._nonterminals:
                for production in glc_productions:
                    origin_prod = production.pop(0)

                    for symbol in production:
                        production.remove(symbol)

                        if key == symbol:
                            self._make_follow_set(production)

            if bckp_follow_sets == self.follow_sets:
                break

    def _make_follow_set(self, production):
        pass
