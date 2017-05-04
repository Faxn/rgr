import unittest

import ply.lex as lex
import lexer



class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        self.myLexer = lex.lex(module=lexer)

    def testA(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        self.myLexer.input("1+1")
        tok = self.myLexer.token()
        print(tok)
        assert tok.type == 'NUMBER'
        tok = self.myLexer.token()
        assert tok.type == 'PLUS'
        tok = self.myLexer.token()
        assert tok.type == 'NUMBER'

if __name__ == "__main__":
    unittest.main() # run all tests
