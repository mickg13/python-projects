class Fraction:

    def _reduce(self,n,d,sign):
        a = abs (n)
        b = abs (d)
        while a % b !=0:
            tempA = a
            tempB = b
            a = tempB
            b = tempA % tempB
        ret_n = abs (n) // b * sign
        ret_d = abs (d) // b
        return (ret_n,ret_d)

    def getNumerator(self):
        return self._numerator

    def getDenomniator(self):
        return self._denomniator

    def __init__(self,numerator,denomniator):

        if(not isinstance(numerator,int)):
            raise TypeError ("The numerator of a Farction must be an integer")

        if(not isinstance(denomniator,int)):
            raise TypeError("The denomniator of a Farction must be an integer")

        if(denomniator == 0):
            raise ZeroDivisionError("The denomniator of a farction can not be zero")

        if (numerator == 0):
             self._numerator = 0
             self._denomniator = 1
        else:
            if (numerator < 0 and denomniator >= 0)or (numerator >=0 and denomniator < 0):
                sign = -1
            else:
                sign = 1
                (self._numerator,self._denomniator) = self._reduce(numerator,denomniator,sign)
    def __repr__(self):
        return str (self._numerator) + "/" + str(self._denomniator)

    def __eq__(self, rhs):
        lhs = self
        return (lhs.getNumerator()== rhs.getNumerator()) and (lhs.getDenomniator() == rhs.getDenomniator)

    def __ne__(self,rhs):
        lhs = self
        return not lhs == rhs

    def __lt__(self,rhs):
        lhs = self
        return lhs.getNumerator() * rhs.getDenomniator() < lhs.getDenomniator()* rhs.getNumerator()
    def __le__(self,rhs):
        lhs = self
        return not rhs < lhs

    def __gt__(self,rhs):
        lhs = self
        return rhs < lhs

    def __ge__(self,rhs):
        lhs = self
        return not rhs > lhs


    def __add__(self, rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenomniator() + rhs.getNumerator() * lhs.getDenomniator()
        den = lhs.getDenomniator() * rhs.getDenomniator()
        return Fraction(num,den)


    def __sub__(self, rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenomniator() - rhs.getNumerator() * lhs.getDenomniator()
        den = lhs.getDenomniator() * rhs.getDenomniator()
        return Fraction(num,den)


    def __mul__(self, rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.Numerator()
        den = lhs.getDenomniator() * rhs.getDenomniator()
        return Fraction(num,den)



    def __truediv__(self, rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenomniator()
        den = lhs.getDenomniator() * rhs.getNumerator()
        return Fraction(num,den)

try:
    x = Fraction (1.1,2.2)
    print("fail")
except:
    print("pass")
try:
    y = Fraction (1,2,1,5)
    print("fail")
except:
    print("pass")

x = 999/1000
print("x is  :",x)

y = 998/1000
print("y is :",y)

answer = 1/1000
print("The answer should be :",answer)

x = Fraction(999,1000)
print(x)

y = Fraction(998,1000)
print(y)

z = x - y
print(z)


x = Fraction (999,1000)
y = Fraction (998,1000)
answer = Fraction (1,1000)
z = x - y
if (z == answer):
  print("pass")
else:
  print("fail")

if (str(z)=="1/1000"):
  print("pass")
else:
  print("fail")

answer = Fraction (1997,1000)
z = x + y
if (z == answer):
  print("pass")
else:
  print("fail")

if (str(z)=="1997/1000"):
  print("pass")
else:
  print("fail")


if (x >= z):
  print("pass")
else:
  print("fail")



D = [1, 2, 4, 6, 5, 9]

D2 = []
prev_pair_diff = -1
D2.append(D[0])

for i in range(1, len(D)):
    print('D[i]', D[i])
    print('Comparing to', D2[-1])
    diff = abs(D[i] - D2[-1])
    print('diff', diff)
    print('previous diff', prev_pair_diff)
    print('D2 before', D2)
    if diff > prev_pair_diff:
      D2.append(D[i])
      prev_pair_diff = diff
    print('D2 after', D2)
    print('=========')

print(D2)

