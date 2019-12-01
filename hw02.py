import numpy as np
import math
from PyOptimizer import CForwardDiff
from PyOptimizer import CBackwardDiff
from PyOptimizer import CCentralDiff
from PyOptimizer import CGradDecent

def Test2VarFun1(x):
    return (x[0]-x[1]+2*(x[0]**2)+2*x[0]*x[1]+x[1]**2)
# x* = [-1, 1.5], f(x*) = -1.25;

def Testfun(x):
    return (x[0]**2 + x[1])

def PowellFun(x):
    f1 = x[0]+10*x[1]
    f2 = ((5.0)**0.5)*(x[2]-x[3])
    f3 = (x[1]-2*x[2])**2
    f4 = ((10.0)**0.5)*((x[0]-x[3])**2)
    return (f1*f1+f2*f2+f3*f3+f4*f4)**0.5
# x* = [0, 0, 0, 0], f(x*) = 0;

def Test2VarFun4(x):
    return -3*x[1]/(x[0]**2+x[1]**2+1)
# x* = [0, 1], f(x*) = -1.5;


def Test2VarFun3(x):
    return -x[0]*x[1]*math.exp(-x[0]**2-x[1]**2)
# x* = [0.7071, 0.7071] or x* = [-0.7071, -0.7071], f(x*) = -0.1839;

a = Testfun
b = Test2VarFun1
c = PowellFun
d = Test2VarFun4
e = Test2VarFun3
# print(b(0.1))

x = [0, 0]
x1 = [-5, 5]
x2 = [2, 1]
x3 = [0, 0, 0.05, 0.1]

# F1 = CForwardDiff(b, x, 2)
# F1.set_percent(0.001)
# F1.GetGrad(x2)

# F2 = CBackwardDiff(b, x2, 2)
# F2.set_percent(0.01)
# F2.GetGrad(x2)

# F3 = CCentralDiff(a, x2, 2)
# F3.set_percent(0.01)
# F3.GetGrad(x2)

# C1 = CGradDecent(b, x, 2)
# C1.RunOptimize()

C2 = CGradDecent(e, x2, 2)
C2.RunOptimize()
