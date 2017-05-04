

from . import lexer
from .parseRoll import parser


def roll(expression : str):
    try:
        tree = parser.parse(expression)
        result, hist = tree.roll()
    except Exception as E:
        return str(E)
    
    return hist

def compile(expression : str):
    tree = parser.parse(expression)
    return tree
