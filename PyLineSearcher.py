import math

class GSSearch:
    def __init__(self, costfun, x = 0, d = 1, eps = 0.01):
        self.__costfun = costfun
        self.__x = x
        self.__d = d
        self.__eps = eps
        self.__alpha_u = 0
        self.__alpha_l = 0
        
        
        

    def set_costfun(self, costfun):
        self.__costfun = costfun
        return self.__costfun 

    def set_x(self, x):
        self.__x = x
        return self.__x

    def set_d(self, d):
        self.__d = d
        return self.__d
        
    def set_eps(self, eps):
        self.__eps =eps
        return self.__eps
    
    def RunSearch(self):        
        alpha_u = self.__alpha_u
        alpha_l = self.__alpha_l        
        x_star = 0
        self.__Phase1()
        self.__Phase2(alpha_u, alpha_l)
        x_star = self.__x        
        # print('X_star = {}'.format(x_star))
        # print('f(X_star) = {}'.format(self.__costfun(x_star)))
        return x_star

 

    def __Phase1(self):
        print('---------------- Phase 1 Start ----------------')        
        delta = self.__eps
        zero = 0
        g = 0
        interval = 0
        alpha_u = self.__costfun([self.__x[i] + g * self.__d[i] for i in range(0, len(self.__d))])
        alpha_l = self.__costfun([self.__x[i] + g * self.__d[i] for i in range(0, len(self.__d))])
        alpha_i = self.__costfun([self.__x[i] + g * self.__d[i] for i in range(0, len(self.__d))])

        while True:
            for i in range(g, g+3):
                sum_u = delta*1.618**i
                alpha_u = alpha_u + sum_u

            for i in range(g, g+1):
                sum_l = delta*1.618**i
                alpha_l = alpha_l + sum_l

            for i in range(g, g+2):
                sum_i = delta*1.618**i
                alpha_i = alpha_i + sum_i

            if self.__costfun([self.__x[i] + delta * self.__d[i] for i in range(0, len(self.__d))]) >= self.__costfun([self.__x[i] + zero * self.__d[i] for i in range(0, len(self.__d))]):
                interval = self.__eps
                alpha_u = self.__eps
                alpha_l = 0
                self.__alpha_u = alpha_u
                self.__alpha_l = alpha_l
                return self.__alpha_u, self.__alpha_l


            if self.__costfun([self.__x[i] + alpha_i * self.__d[i] for i in range(0, len(self.__d))]) < self.__costfun([self.__x[i] + alpha_u * self.__d[i] for i in range(0, len(self.__d))]) and self.__costfun([self.__x[i] + alpha_i * self.__d[i] for i in range(0, len(self.__d))]) < self.__costfun([self.__x[i] + alpha_l * self.__d[i] for i in range(0, len(self.__d))]):
                interval = alpha_u - alpha_l
                
                #print('g ={}'.format(g))
                print('interval = {}'.format(interval))
                print('alpha_i = {}'.format(alpha_i))
                print('alpha_u = {}'.format(alpha_u))
                print('alpha_l = {}'.format(alpha_l))
                print('---------------- Phase 1 End ----------------')
                self.__alpha_u = alpha_u
                self.__alpha_l = alpha_l
                return self.__alpha_u, self.__alpha_l                
                

            else:
                g +=1         

    def __Phase2(self, alpha_u, alpha_l):
        rho = 0.38197
        delta = self.__eps
        alpha_u = self.__alpha_u
        alpha_l = self.__alpha_l        

        ml = delta / (alpha_u - alpha_l)
        iteration_number = math.ceil(math.log(ml) / math.log(0.61803)) 

        print('---------------- Phase 2 Start ----------------')
        print('iteration_number = {}'.format(iteration_number))

        for i in range(iteration_number+1):
            a1 = alpha_l + rho * (alpha_u - alpha_l)
            #f(a1) = self.Equations(a1)
            b1 = alpha_l + (1 - rho) * (alpha_u - alpha_l)
            #f(b1) = self.Equations(b1)
            if self.__costfun([self.__x[i] + a1 * self.__d[i] for i in range(0, len(self.__d))]) < self.__costfun([self.__x[i] + b1 * self.__d[i] for i in range(0, len(self.__d))]):
                alpha_u = b1
                #b1 = a1           
            if self.__costfun([self.__x[i] + a1 * self.__d[i] for i in range(0, len(self.__d))]) > self.__costfun([self.__x[i] + b1 * self.__d[i] for i in range(0, len(self.__d))]):
                alpha_l = a1
                #a1 = b1

            if self.__costfun([self.__x[i] + a1 * self.__d[i] for i in range(0, len(self.__d))]) == self.__costfun([self.__x[i] + b1 * self.__d[i] for i in range(0, len(self.__d))]):
                alpha_l = a1
                alpha_u = b1
                iteration_number += 1

            i = i+1
        if alpha_u - alpha_l < self.__eps:
            x_star = (alpha_u + alpha_l) / 2
            print(x_star)
            self.__x = x_star
            print('---------------- Phase 2 End ----------------')
            return self.__x
        else:
            print('error')

            print('---------------- Phase 2 End ----------------')


class CFiSearch:
    def __init__(self, costfun, x = 0, d = 1, eps = 0.01):
        self.__costfun = costfun
        self.__x = x
        self.__d = d
        self.__eps = eps
        self.__alpha_u = 0
        self.__alpha_l = 0
        
        
        

    def set_costfun(self, costfun):
        self.__costfun = costfun
        return self.__costfun 

    def set_x(self, x):
        self.__x = x
        return self.__x

    def set_d(self, d):
        self.__d = d
        return self.__d
        
    def set_eps(self, eps):
        self.__eps =eps
        return self.__eps
    
    def RunSearch(self):
        
        alpha_u = self.__alpha_u
        alpha_l = self.__alpha_l        
        x_star = 0
        self.__Phase1()
        self.__Phase2(alpha_u, alpha_l)
        x_star = self.__x        
        # print('X_star = {}'.format(x_star))
        # print('f(X_star) = {}'.format(self.__costfun(x_star)))
        return x_star


    def __Phase1(self):
        print('---------------- Phase 1 Start ----------------')
        delta = self.__eps
        g = 0
        zero = 0
        interval = 0
        print('x',[self.__x[i] + g * self.__d[i] for i in range(0, len(self.__d))])
        alpha_u = self.__costfun([self.__x[i] + g * self.__d[i] for i in range(0, len(self.__d))])
        alpha_l = self.__costfun([self.__x[i] + g * self.__d[i] for i in range(0, len(self.__d))])
        alpha_i = self.__costfun([self.__x[i] + g * self.__d[i] for i in range(0, len(self.__d))])

        while True:
            print(g)
            for i in range(g, g+3):                
                sum_u = delta*1.618**i
                alpha_u = alpha_u + sum_u                

            for i in range(g, g+1):
                sum_l = delta*1.618**i
                alpha_l = alpha_l + sum_l

            for i in range(g, g+2):
                sum_i = delta*1.618**i
                alpha_i = alpha_i + sum_i

            if self.__costfun([self.__x[i] + delta * self.__d[i] for i in range(0, len(self.__d))]) >= self.__costfun([self.__x[i] + zero * self.__d[i] for i in range(0, len(self.__d))]):
                interval = self.__eps
                alpha_u = self.__eps
                alpha_l = 0
                self.__alpha_u = alpha_u
                self.__alpha_l = alpha_l
                return self.__alpha_u, self.__alpha_l


            if self.__costfun([self.__x[i] + alpha_i * self.__d[i] for i in range(0, len(self.__d))]) < self.__costfun([self.__x[i] + alpha_u * self.__d[i] for i in range(0, len(self.__d))]) and self.__costfun([self.__x[i] + alpha_i * self.__d[i] for i in range(0, len(self.__d))]) < self.__costfun([self.__x[i] + alpha_l * self.__d[i] for i in range(0, len(self.__d))]):
                interval = alpha_u - alpha_l                
                #print('g ={}'.format(g))
                print('interval = {}'.format(interval))
                print('alpha_i = {}'.format(alpha_i))
                print('alpha_u = {}'.format(alpha_u))
                print('alpha_l = {}'.format(alpha_l))
                print('---------------- Phase 1 End ----------------')
                self.__alpha_u = alpha_u
                self.__alpha_l = alpha_l
                return self.__alpha_u, self.__alpha_l                
                

            
            else:
                # print('alpha_i = {}'.format(alpha_i))
                # print('alpha_u = {}'.format(alpha_u))
                # print('alpha_l = {}'.format(alpha_l))
                g = g + 1
                

    def __Phase2(self, alpha_u, alpha_l):

        def fibonacci(n):
            if n == 0:
                return 1
            elif n == 1:
                return 1
            return fibonacci(n-1) + fibonacci(n-2)

        def get_fibosquence(fibonacci, x):
            i = 1
            while fibonacci(i) <= x:
                i += 1
            return i - 1

        epsilon = self.__eps
        rho = 0.5 - epsilon
        iteration_number = 0

        delta = self.__eps
        alpha_u = self.__alpha_u
        alpha_l = self.__alpha_l        

        ml = delta / (alpha_u - alpha_l)
        F = math.ceil((1 + 2*epsilon) / ml)
        iteration_number = get_fibosquence(fibonacci, F)
        fibo = iteration_number

        print('---------------- Phase 2 Start ----------------')
        print('iteration_number = {}'.format(iteration_number))

        for i in range(iteration_number+1):
            rho = 1 - fibonacci(fibo) / fibonacci(fibo+1)
            if fibonacci(fibo) / fibonacci(fibo+1) <= 0.5:
                rho = 0.5 - epsilon         
            a1 = alpha_l + rho * (alpha_u - alpha_l)
            #f(a1) = self.Equations(a1)
            b1 = alpha_l + (1 - rho) * (alpha_u - alpha_l)
            #f(b1) = self.Equations(b1)
            if self.__costfun([self.__x[i] + a1 * self.__d[i] for i in range(0, len(self.__d))]) < self.__costfun([self.__x[i] + b1 * self.__d[i] for i in range(0, len(self.__d))]):
                alpha_u = b1
                #b1 = a1           
            if self.__costfun([self.__x[i] + a1 * self.__d[i] for i in range(0, len(self.__d))]) > self.__costfun([self.__x[i] + b1 * self.__d[i] for i in range(0, len(self.__d))]):
                alpha_l = a1
                #a1 = b1

            if self.__costfun([self.__x[i] + a1 * self.__d[i] for i in range(0, len(self.__d))]) == self.__costfun([self.__x[i] + b1 * self.__d[i] for i in range(0, len(self.__d))]):
                alpha_l = a1
                alpha_u = b1
                iteration_number += 1
            fibo = iteration_number - 1
            i = i+1
        if alpha_u - alpha_l < self.__eps:
            x_star = (alpha_u + alpha_l) / 2
            print('........................')
            self.__x = x_star
            print('---------------- Phase 2 End ----------------')
            return self.__x
        else:
            print('error')

            print('---------------- Phase 2 End ----------------')
        
        



        
        