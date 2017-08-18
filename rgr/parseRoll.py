import ply.yacc as yacc
import sys,string,random, re
try:
    from .ast import *
    from . import lexer
except SystemError:
    from ast import *
    import lexer
tokens = lexer.tokens

########################################################################
#Parser

precedence = (  
    ('left', 'EXPRESS', 'ISUM', 'c'),
    ('left', '#', 'GTE'),
    #('left', 'SUM'),
    ('left','+', '-'),
    #('left', 'TIMES'),
    ('nonassoc', 'KEEP', 'k'),
    ('nonassoc', 'd')
)

# t is a token array, t[0] is what the statment evaluates to and t[1:] 
# are the operands matching the statment.

def p_statement_expr(t):
    '''statement : expression'''
    t[0] = Statment(t[1])

def p_expression(t):
    """expression : scalar %prec EXPRESS"""
    t[0] = t[1]

def p_scalar_number(t):
    'scalar : INTEGER'
    t[0] = Integer(t[1])
  
def p_scalar_binop(t):
    """scalar : scalar '+' scalar
              | scalar '-' scalar"""
    t[0] = BinOp(t[1], t[2], t[3])

def p_dice(t):
    "list : scalar 'd' scalar"
    t[0] = Dice(t[1], t[3])

def p_unary_die(t):
    "list : 'd' scalar"
    t[0] = Dice(Integer(1), t[2])

def p_scalar_group(p):
    "scalar : '(' scalar ')'"
    p[0] = p[2]

# keep
def p_high_keep(t):
    "list : HIGHEST scalar OF list %prec KEEP"
    t[0] = Keep('highest', t[2], t[4])

def p_low_keep(t):
    "list : LOWEST scalar OF list %prec KEEP"
    t[0] = Keep('lowest', t[2], t[4])

def p_high_keep_short(t):
    "list : list 'k' scalar"
    t[0] = Keep('highest', t[3], t[1])

#List concat/literals
#def p_list(t):
#    "list: scalar ',' scalar"
#    t[0]


# filter
def p_filter(t):
    "list : list GTE scalar"
    t[0] = Filter(t[1], 'gte', t[3])

# repeat
def p_repeat(t):
    "list : scalar '#' expression"
    t[0] = Repeat(t[1], t[3])

def p_count(t):
    "scalar : 'c' list"
    t[0] = Count(t[2])

def p_implicit_sum(t):
    "scalar : list %prec ISUM"
    t[0] = SumList(t[1])

# error
def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc(debug=True)

