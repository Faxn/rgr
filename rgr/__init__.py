

from . import lexer
from .parseRoll import parser


def roll(expression : str):
    "Runs the dice expression provided and returns long form result"
    try:
        tree = parser.parse(expression)
        result, hist = tree.roll()
    except Exception as E:
        return str(E)
    
    return result, hist, tree

def compile(expression : str):
    tree = parser.parse(expression)
    return tree

try:
    from .rgrcog import RGR

    def setup(bot):
        bot.add_cog(RGR(bot))
except ModuleNotFoundError as e:
    def setup(bot):
        raise Exception(str(e), e)
    pass
