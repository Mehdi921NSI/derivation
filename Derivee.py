from sympy import *
x = Symbol('x')
a = 3*x
b = 3*x**2+4*x+2
c = 1/x
d = (3*x+3)/(4*x**2+7*x+6)
print(type(d))
def derivee(y):
    yp = y.diff(x)
    print("la dérivée est :", yp)
derivee(d)

   