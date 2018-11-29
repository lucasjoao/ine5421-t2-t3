import unittest
from src.parser import Parser


class ParserTests(unittest.TestCase):
    def test_make_first_set_01(self):
        # example from slide
        parser = Parser('data/book_glc_01', True)
        right_result = {'S': {'a', 'b', 'c', 'd'},
                        'B': {'a', 'b', 'd', '&'},
                        'A': {'a', '&'}}
        self.assertDictEqual(parser.first_sets, right_result)

    def test_make_first_set_02(self):
        # example from slide
        parser = Parser('data/book_glc_02', True)
        right_result = {'S': {'a', 'b', 'c', 'd'},
                        'B': {'a', 'b', 'c', 'd'},
                        'A': {'a', '&'},
                        'C': {'c', '&'}}
        self.assertDictEqual(parser.first_sets, right_result)

    def test_make_follow_set_01(self):
        # example from slide
        parser = Parser('data/book_glc_01', True)
        right_result = {'S': {'$'},
                        'B': {'c'},
                        'A': {'b', 'a', 'd', 'c'}}
        self.assertDictEqual(parser.follow_sets, right_result)

    def test_make_follow_set_02(self):
        # example from slide
        parser = Parser('data/book_glc_02', True)
        right_result = {'S': {'$'},
                        'B': {'c', '$'},
                        'A': {'b', 'a', 'c', 'd'},
                        'C': {'d', '$'}}
        self.assertDictEqual(parser.follow_sets, right_result)

    def test_make_parsing_table_01(self):
        # example from slide
        parser = Parser('data/book_glc_03', True)
        right_result = {('E', 'id'): ['T', 'Z'],
                        ('E', 'neg'): ['T', 'Z'],
                        ('Z', 'v'): ['v', 'T', 'Z'],
                        ('Z', '$'): ['&'],
                        ('T', 'id'): ['F', 'W'],
                        ('T', 'neg'): ['F', 'W'],
                        ('W', 'v'): ['&'],
                        ('W', 'til'): ['til', 'F', 'W'],
                        ('W', '$'): ['&'],
                        ('F', 'id'): ['id'],
                        ('F', 'neg'): ['neg', 'F']}
        self.assertDictEqual(parser.parsing_table, right_result)

if __name__ == '__main__':
    unittest.main()
