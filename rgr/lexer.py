import ply.lex as lex


########################################################################################## 
#lexxer

tokens = (
     'INTEGER',
     'HIGHEST', 'LOWEST', 'OF'
)

literals = ['+', '-', 'd', '(', ')', '#', 'k']

# Magic token for things the parser silently ignores.
t_ignore = " \t"

#tokens


t_HIGHEST = r'(highest)|(best)'
t_LOWEST =  r'(lowest)|(worst)'
t_OF = r'of'
'''
#dice
t_DICE = r'd'
t_ROLL = r'r'

#other
t_SUM = r'e'
t_COMMA = r','
'''

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
     #print("Illegal character '%s'" % t.value[0])
     raise SyntaxError("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
     

lexer = lex.lex()
