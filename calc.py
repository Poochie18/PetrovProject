from nsk import LCM

class Calculator:
    def __init__(self, first, second):
        if second == 0:
            raise ZeroDivisionError
        self.first = first
        self.second = second


    def div(self,b):
        return self / b

    def add(self,b):
        nsk = Calculator.simply(self.second, b.second)
        new_chlen1 = self.first*(Calculator.div(nsk,self.second))
        new_chlen2 = b.first*(Calculator.div(nsk, b.second))
        return Calculator.div(new_chlen1+new_chlen2, nsk)

    def simply(self,b):
        return LCM.lcm(self, b)
try:
    a = Calculator(2, 7)
    c = Calculator(1, 4)
    res = Calculator.add(a,c)
    print(Calculator.simply(a,c))
except:
    print('Zero')

