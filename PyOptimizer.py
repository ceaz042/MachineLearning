import  math
from PyLineSearcher import GSSearch
from PyLineSearcher import CFiSearch


class CForwardDiff:
    def __init__(self, costfun, x, dim, eps = 1e-5, percent = 1e-4):
        self.__costfun = costfun
        self.__x = x
        self.__dim = dim
        self.__eps =eps
        self.__percent = percent


    def set_costfun(self, costfun):
        self.__costfun = costfun
        return self.__costfun 

    def set_x(self, x):
        self.__x = x
        return self.__x

    def set_d(self, dim):
        self.__dim = dim
        return self.__dim
        
    def set_eps(self, eps):
        self.__eps =eps
        return self.__eps

    def set_percent(self, percent):
        self.__percent = percent

    def GetGrad(self, x):   
        d = []
        fun = self.__costfun          
        x0 = self.__x.copy()
        x1 = self.__x.copy()
        g = fun(x0)        
        for index in range(0, len(x)):                                   
            h = x[index] * self.__percent + self.__eps            
            x1[index] = x1[index] + h
            print('x',x1)            
            d.append((fun(x1) - g)/h)
            x1[index] = x0[index]
        print('d', d)        
        return d

class CBackwardDiff:
    def __init__(self, costfun, x, dim, eps = 1e-5, percent = 1e-4):
        self.__costfun = costfun
        self.__x = x
        self.__dim = dim
        self.__eps = eps
        self.__percent = percent


    def set_costfun(self, costfun):
        self.__costfun = costfun
        return self.__costfun 

    def set_x(self, x):
        self.__x = x
        return self.__x

    def set_d(self, dim):
        self.__dim = dim
        return self.__dim
        
    def set_eps(self, eps):
        self.__eps =eps
        return self.__eps

    def set_percent(self, percent):
        self.__percent = percent

    def GetGrad(self, x):
        self.__x = x
        d = []
        fun = self.__costfun         
        x0 = self.__x.copy()
        x1 = self.__x.copy()
        g = fun(x0)        
        for index in range(0, len(x)):                     
            h = x[index] * self.__percent + self.__eps
            x1[index] = x1[index] - h                     
            d.append((g - fun(x1) )/ h )
            x1[index] = x0[index]                   
        print('d', d)
        return d

class CCentralDiff:
    def __init__(self, costfun, x, dim, eps = 1e-5, percent = 1e-4):
        self.__costfun = costfun
        self.__x = x
        self.__dim = dim
        self.__eps =eps
        self.__percent = percent


    def set_costfun(self, costfun):
        self.__costfun = costfun
        return self.__costfun 

    def set_x(self, x):
        self.__x = x
        return self.__x

    def set_d(self, dim):
        self.__dim = dim
        return self.__dim
        
    def set_eps(self, eps):
        self.__eps =eps
        return self.__eps

    def set_percent(self, percent):
        self.__percent = percent

    def GetGrad(self, x):        
        d = []
        print('start')
        fun = self.__costfun        
        self.__x = x
        x_forward = self.__x.copy()        
        x_backward = self.__x.copy()
        x_0 = self.__x.copy()
        for index in range(0, len(x)):            
            h = x_0[index] * self.__percent + self.__eps
            x_forward[index] = x_forward[index] + (h/2)                     
            x_backward[index] = x_backward[index] - (h/2)            
            # print('h', h)
            # print('x_forward',x_forward)
            # print('x_backward', x_backward)
            d.append((fun(x_forward)-fun(x_backward))/h)      
            x_forward[index] = x_0[index]             
            x_backward[index] = x_0[index]              
        print('d', d)
        return d

class CGradDecent:
    def __init__(self, costfun, x0, dim, Gradient = 'Backward',LineSearch = 'FiS', MinNorm = 0.001, MaxIter = 1000):
        self.__x0 = x0
        self.__dim = dim
        self.__MaxIter = MaxIter
        self.__MinNorm = MinNorm        
        self.__costfun = costfun
        self.__LineSearch = LineSearch
        self.__Gradient = Gradient

    def set_costfun(self, costfun):
        self.__costfun = costfun
        return self.__costfun

    def set_x(self, x0):
        self.__x0 = x0
        return self.__x0

    def set_d(self, dim):
        self.__dim = dim
        return self.__dim

    def set_MaxIter(self, MaxIter):
        self.__MaxIter = MaxIter
        return self.__MaxIter

    def set_MinNorm(self, MinNorm):
        self.__MinNorm = MinNorm
        return self.__MinNorm

    def RunOptimize(self):        
        
        x = self.__x0
        k = 0
        d = 1        
        fun = self.__costfun

        if (self.__LineSearch == "FiS"):
            LineSearch = CFiSearch(fun, x, d, eps=0.01)
        else:
            LineSearch = GSSearch(fun, x, d)

        if (self.__Gradient == 'Forward'):
            Diff = CForwardDiff(fun, x, self.__dim)
        elif (self.__Gradient == 'Backward'):
            Diff = CBackwardDiff(fun, x, self.__dim)
        else:
            Diff = CCentralDiff(fun, x, self.__dim)

        grad_Magnitude = math.inf

        while (k < self.__MaxIter):
            print('Optimizer Iter[', k, ']')

            if (k!=0):
                Diff.set_x = x
            # print('x0',x)
            print('Getting Gradient')
            grad = Diff.GetGrad(x)

            grad_Magnitude = math.sqrt(math.fsum([i*i for i in grad]))
            print('||Gradient||: ',grad_Magnitude)
            if (grad_Magnitude < self.__MinNorm):
                print("Gradient < MinNorm", grad_Magnitude)
                print('x_star', x)
                print('f(x_star)', self.__costfun(x))
                return x

            d = [-i for i in grad]            
            
            if (k != 0):
                LineSearch.set_x(x)
            
            # LineSearch.d = d
            LineSearch.set_d(d)
            #timeStart = time.time()
            print('LineSearch')
            alpha = LineSearch.RunSearch()
            #timeEnd = time.time()
            #print('Run Search Cost: ', timeEnd - timeStart)
            print('step size', alpha)
            x = [x[i] + alpha * d[i]for i in range(0, len(x))]            
            print('X:', x)
            #print('loss', fun(x))
            

            k += 1

            
        
        return x






