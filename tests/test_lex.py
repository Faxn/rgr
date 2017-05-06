import unittest

import ply.lex as lex
from rgr import lexer

class LexUnit(unittest.TestCase):

    def setUp(self):
        self.myLexer = lex.lex(module=lexer)

    def test_1p1(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        self.myLexer.input("1+1")
        tok = self.myLexer.token()
        print(tok)
        assert tok.type == 'INTEGER'
        tok = self.myLexer.token()
        assert tok.type == '+'
        tok = self.myLexer.token()
        assert tok.type == 'INTEGER'

if __name__ == "__main__":
    unittest.main() # run all tests
