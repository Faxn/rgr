
import random

class Expr: pass

class BinOp(Expr):
    def __init__(self,left,op,right):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op
    def roll(self):
        left,  lhist = self.left.roll()
        right, rhist = self.right.roll()
        result = None
        if self.op == '+':
            result = left+right
        elif self.op == '-':
            result = left-right
        if(self.left.type == self.right.type and self.right.type == 'number'):
            return result, '%d %s %d = %d' % (left, self.op, right, result)
        else:
            return result, '(%s) %s (%s) = %d %s %d = %d' % (lhist, self.op, rhist, left, self.op, right, result)

class Integer(Expr):
    def __init__(self,value):
        self.type = "number"
        self.value = value
    def roll(self):
        return self.value, self.value


class Dice(Expr):
    def __init__(self, left, right):
        self.type = 'dice'
        self.left = left
        self.right = right
    def roll(self):
        number, lhist = self.left.roll()
        side, rhist   = self.right.roll()
        ret = []
        i = 0
        while(number > i):
            ret.append(random.randint(1,side))
            i += 1
        if(self.left.type == self.right.type and self.right.type == 'number'):
            return ret, '%dd%d ≞ %r' % (number, side, ret)
        else:
            return ret, '(%s)d(%s) = %dd%d ≞ %r' % (lhist, rhist,number, side, ret)

class SumList(Expr):
    def __init__(self, l):
        self.type = "sum"
        self.l = l
    def roll(self):
        l, hist = self.l.roll()
        t = sum(l)
        if len(l) > 1:
            return t, 'Σ(%s) = Σ%r = %d' % (hist, l, t)
        else:
            return t, '%s = %d'  % (hist, t)
        
class Keep(Expr):
    def __init__(self, f, count, l):
        self.type = "filter"
        self.f = f
        self.count = count
        self.l = l
    def roll(self):
        count, chist = self.count.roll()
        l, lhist = self.l.roll()
        pre = "%s %s of %s " % (self.f, chist, lhist)
        mid = "["
        if self.f == "highest":
            selected = sorted(l)[len(l)-count:]
        elif self.f == "lowest":
            selected = sorted(l)[:count]
        res = []
        for i in l:
            if i in selected:
                res.append(i)
                mid += "**%d**, " % i
                selected.remove(i)
            else:
                mid += "%d, " % i
        mid = mid[:-2] + ']'
        return res, "%s = %s = %r" % (pre, mid, res)
        
class Repeat(Expr):
    def __init__(self, count, expression):
        self.type = "repeat"
        self.count = count
        self.expression = expression
    def roll(self):
        count, chist = self.count.roll()
        result = []
        history = "(%s = %d)#\n" % (chist, count)
        while(count > 0):
            count -= 1
            resi, histi = self.expression.roll()
            history += "%s\n" % (histi)
            result.append(resi)
        return result, history

class Filter(Expr):
    def __init__(self, l, test):
        self.l = l
        self.test = test
