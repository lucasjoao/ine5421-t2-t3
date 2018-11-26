import unittest
from src.parser import Parser


class ParserTests(unittest.TestCase):
    def test_make_first_set_01(self):
        # example from slide
        parser = Parser('data/test_make_first_set_01', True)
        right_result = {'S': {'a', 'b', 'c', 'd'},
                        'B': {'a', 'b', 'd', '&'},
                        'A': {'a', '&'}}
        self.assertDictEqual(parser.first_sets, right_result)

    def test_make_first_set_02(self):
        # example from slide
        parser = Parser('data/test_make_first_set_02', True)
        right_result = {'S': {'a', 'b', 'c', 'd'},
                        'B': {'a', 'b', 'c', 'd'},
                        'A': {'a', '&'},
                        'C': {'c', '&'}}
        self.assertDictEqual(parser.first_sets, right_result)


if __name__ == '__main__':
    unittest.main()