import unittest
from src.parser import Parser


class ParserTests(unittest.TestCase):
    def test_make_first_set_01(self):
        # example from slide
        parser = Parser('data/test_make_first_set_01', True)
        print(parser.first_sets)

    def test_make_first_set_02(self):
        # example from slide
        parser = Parser('data/test_make_first_set_02', True)
        print(parser.first_sets)

if __name__ == '__main__':
    unittest.main()
