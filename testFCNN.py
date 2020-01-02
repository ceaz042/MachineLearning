from scipy.linalg import norm
import numpy as np
import math
# from PyOptimizer import CGradDecent
# from PyLineSearcher import CFiSearch
# from PyLineSearcher import GSSearch
# from FCNNmodule import NeuronNetwork

## Test of FCNN creation
weights_arrs = [[[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7,0.8,0.9]], # init weights of the 1st neuron layer
[[1.1,1.2,1.3],[1.4,1.5,1.6],[1.7,1.8,1.9], [1.3, 1.2, 1.1]], # init weights of the 2nd neuron layer
[[2.1,2.2,2.3,2.4], [2.5,2.6,2.7,2.8]]] # init weights of the 3rd neuron layer
bias_arr = [[0.1,0.2,0.3], # init biases of the 1st neuron layer
[1.1,1.2,1.3, 1.4], # init biases of the 2nd neuron layer
[2.1,2.2]] # init biases of the 3rd neuron layer
# nn = NeuronNetwork(weights_arrs, bias_arr)
# nn.inspect()
intputs = [0.1, 0.2, 0.3]

def sigmoid(x):
    return 1/(1 + math.exp(-x))

# print('Layers :', len(weights_arrs))
# print('NeuronLayer 0')
# print('Neurons :', len(weights_arrs[0]))
# for j in range(0, len(weights_arrs[0])):
#     print('Neuron ', j)
#     for i in range(0, len(weights_arrs[0][j])):
#         print('Weight :', weights_arrs[0][j][i])
#     print('bias :', bias_arr[0][j])
# print('NeuronLayer 1')
# print('Neurons :', len(weights_arrs[1]))
# for j in range(0, len(weights_arrs[1])):
#     print('Neuron ', j)
#     for i in range(0, len(weights_arrs[1][j])):
#         print('Weight :', weights_arrs[1][j][i])
#     print('bias :', bias_arr[1][j])
# print('NeuronLayer 2')
# print('Neurons :', len(weights_arrs[2]))
# for j in range(0, len(weights_arrs[2])):
#     print('Neuron ', j)
#     for i in range(0, len(weights_arrs[2][j])):
#         print('Weight :', weights_arrs[2][j][i])
#     print('bias :', bias_arr[2][j])

        # yh1 = activation(w11*i1 + w21*i2 + w31*i3 + b1)
        # yh2 = activation(w21*i1 + w22*i2 + w32*i3 + b1)
        # yh3 = activation(w31*i1 + w32*i2 + w33*i3 + b1)
        # yo = activation(h1*yh1 + h2*yh2 + h3*yh3 + b2)

activation = sigmoid
yh_1st = []
#1st hidden layer
for i in range(0, len(weights_arrs[1])):
    yh = 0    
    for j in range(0, len(weights_arrs[1][i])):        
        yh_p = intputs[j]*weights_arrs[1][i][j]
        yh = yh + yh_p
        print('yh',yh)
    yh_0 = activation(yh + bias_arr[1][i])
    yh_1st.append(yh_0)
    print(yh_1st)
y_output = []
#output
for i in range(0, len(weights_arrs[2])):
    yo = 0
    for j in range(0, len(weights_arrs[2][i])):        
        yo_p = yh_1st[j]*weights_arrs[2][i][j]
        yo = yo + yo_p
        print('yo',yo)
    yo_0 = activation(yo + bias_arr[2][i])
    y_output.append(yo_0)
    print(y_output)
    


    




