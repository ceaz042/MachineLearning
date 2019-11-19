from PyOptimizer import CForwardDiff
from PyOptimizer import CBackwardDiff
from PyOptimizer import CCentralDiff

def Test2VarFun1(x):
    return (x[0]-x[1]+2*(x[0]**2)+2*x[0]*x[1]+x[1]**2)
# x* = [-1, 1.5], f(x*) = -1.25;

def Testfun(x):
    return (x[0]**2 + x[1])

a = Testfun
b = Test2VarFun1


x = [2, 1]

# F1 = CForwardDiff(a, x, 2)
# F1.set_percent(0.01)

# F1.GetGrad(x)
# F2 = CBackwardDiff(a, x, 2)
# F2.set_percent(0.01)
# F2.GetGrad(x)

F3 = CCentralDiff(a, x, 2)
F3.set_percent(0.01)
F3.GetGrad(x)