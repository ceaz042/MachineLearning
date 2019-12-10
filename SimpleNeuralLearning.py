from scipy.linalg import norm
import numpy as np
import math
from PyOptimizer import CGradDecent
from PyLineSearcher import CFiSearch

def sigmoid(x):
    return 1/(1 + math.exp(-x))

activation = sigmoid
x0 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
x1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]

def fun_learning(x):
    train = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]]
    train_1 = [[row[i] for row in train] for i in range (4)]
    i1 = train_1[0]
    i2 = train_1[1]
    i3 = train_1[2]
    yd = train_1[3]    
    w11 = x[0]
    w12 = x[1]
    w13 = x[2]
    b1 = x[3]
    w21 = x[4]
    w22 = x[5]
    w23 = x[6]
    b2 = x[7]
    w31 = x[8]
    w32 = x[9]
    w33 = x[10]
    b3 = x[11]
    w41 = x[12]
    w42 = x[13]
    w43 = x[14]
    b4 = x[15]
    # w11 = x[0]
    # w12 = x[1]
    # w13 = x[2]
    # w21 = x[3]
    # w22 = x[4]
    # w23 = x[5]
    # w31 = x[6]
    # w32 = x[7]
    # w33 = x[8]
    # w41 = x[9]
    # w42 = x[10]
    # w43 = x[11]
    
    x1 = [w11*i1[i] + w21*i2[i] + w31*i3[i] + b1  for i in range(0, len(i1))]    
    x2 = [w12*i1[i] + w22*i2[i] + w32*i3[i] + b2  for i in range(0, len(i1))]
    x3 = [w13*i1[i] + w23*i2[i] + w33*i3[i] + b3  for i in range(0, len(i1))]    
    z1 = [activation(x1[i]) for i in range(0, len(x1))]
    z2 = [activation(x2[i]) for i in range(0, len(x2))]
    z3 = [activation(x2[i]) for i in range(0, len(x3))]    
    z4 = [w41*z1[i] + w42*z2[i] + w43*z3[i] + b4 for i in range(0, len(z1))]
    err = [yd[i] - activation(z4[i]) for i in range(0, len(z4))]    
    f = np.linalg.norm(err) 
    # print(err)
    print(f)
    return f

def fun_prediction(x, in1, in2, in3):        
    i1 = in1
    i2 = in2
    i3 = in3    
    w11 = x[0]
    w12 = x[1]
    w13 = x[2]
    b1 = x[3]
    w21 = x[4]
    w22 = x[5]
    w23 = x[6]
    b2 = x[7]
    w31 = x[8]
    w32 = x[9]
    w33 = x[10]
    b3 = x[11]
    w41 = x[12]
    w42 = x[13]
    w43 = x[14]
    b4 = x[15]
    # w11 = x[0]
    # w12 = x[1]
    # w13 = x[2]
    # w21 = x[3]
    # w22 = x[4]
    # w23 = x[5]
    # w31 = x[6]
    # w32 = x[7]
    # w33 = x[8]
    # w41 = x[9]
    # w42 = x[10]
    # w43 = x[11]
    
    x1 = [w11*i1[i] + w21*i2[i] + w31*i3[i] + b1 for i in range(0, len(i1))]    
    x2 = [w12*i1[i] + w22*i2[i] + w32*i3[i] + b2 for i in range(0, len(i2))]
    x3 = [w13*i1[i] + w23*i2[i] + w33*i3[i] + b3 for i in range(0, len(i3))]    
    z1 = [activation(x1[i]) for i in range(0, len(x1))]
    z2 = [activation(x2[i]) for i in range(0, len(x2))]
    z3 = [activation(x2[i]) for i in range(0, len(x3))]
    z4 = [w41*z1[i] + w42*z2[i] + w43*z3[i] + b4 for i in range(0, len(z1))]    
    f = [activation(z4[i]) for i in range(0, len(z4))]    
    print(f)
G = CGradDecent(fun_learning, x0, len(x0))
x_opt = G.RunOptimize()

fun_learning(x0)
fun_learning(x_opt)
fun_prediction(x0, [1, 0, 1], [1, 1, 0], [0, 0, 0]) #out:0, 1, 1, 0
fun_prediction(x_opt, [1, 0, 1], [1, 1, 0], [0, 0, 0])



