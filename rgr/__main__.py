import sys
import readline
import traceback

from . import lexer
from .parseRoll import parser

if (sys.version_info.major < 3):
    print("RGR requires at least python 3.")
    sys.exit(1)


buff=""
try:
    while True:
        line = input("RGR>").strip()
        if( line == "quit" ):
            sys.exit()
        if( line == ""):
            line=buff
        try:
            roller = parser.parse(line)
            result, history = roller.roll()
            print(result)
            print(history)
        except Exception as E:
            traceback.print_exc()
        buff=line
        
except EOFError:
    print()
