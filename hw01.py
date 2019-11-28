from PyLineSearcher import GSSearch
from PyLineSearcher import CFiSearch

def Testfun1(x):
    return x**4 - 14*(x**3) + 60*(x**2) -70*x

def Testfun2(x):
    return (-x*(108-x**2))/4

a = Testfun1
b = Testfun2

# G1 = GSSearch(b)
# G1.set_eps(0.3)

# G1.RunSearch()

C1 = CFiSearch(b)
C1.set_eps(0.3)



C1.RunSearch()