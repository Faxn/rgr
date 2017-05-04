import unittest

import ply.lex as lex
import lexer
lex.lex(module=lexer)
import lexer
from parseRoll import parser


class SimpleTestCase(unittest.TestCase):

    
    def testAddtion(self):
        """Basic Addtion"""
        out = parser.parse("1+1").roll()
        assert out == 2
        
        

if __name__ == "__main__":
    unittest.main() # run all tests
