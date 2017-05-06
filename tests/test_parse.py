import unittest

import ply.lex as lex
from rgr import lexer
lex.lex(module=lexer)
from rgr.parseRoll import parser


class ParseUnit(unittest.TestCase):
    pass

    
    
        

if __name__ == "__main__":
    unittest.main() # run all tests
