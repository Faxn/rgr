import sys
import readline
import traceback
import argparse

from . import lexer
from .parseRoll import parser

if (sys.version_info.major < 3):
    print("RGR requires at least python 3.")
    sys.exit(1)

ap = argparse.ArgumentParser(description='roll dice.')
ap.add_argument('--interactive', '-i', action='store_true', help='run in interactive mode')
ap.add_argument('roll', default='1d6', nargs=argparse.REMAINDER, help='a roll to evaluate now.')

args = ap.parse_args()



if args.interactive:
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
else:
    roller = parser.parse(' '.join(args.roll))
    result, history = roller.roll()
    print(result)
    print(history)
