from scipy.linalg import norm
import numpy as np
import math
from PyOptimizer import CGradDecent
from PyLineSearcher import CFiSearch
from PyLineSearcher import GSSearch

class Neuron:
    def __init__(self, weights_vec, bias):
        self.weights_vec = weights_vec
        self.bias = bias

    def forward(self, inputs):
        activation = __sigmoid        
        yh_1st = []
        #1st hidden layer
        for i in range(0, len(self.weights_vec[1])):
            yh = 0    
            for j in range(0, len(self.weights_vec[1][i])):        
                yh_p = intputs[j]*self.weights_vec[1][i][j]
                yh = yh + yh_p
                print('yh',yh)
            yh_0 = activation(yh + self.bias[1][i])
            yh_1st.append(yh_0)
            print(yh_1st)
        y_output = []
        #output
        for i in range(0, len(self.weights_vec[2])):
            yo = 0
            for j in range(0, len(self.weights_vec[2][i])):        
                yo_p = yh_1st[j]*self.weights_vec[2][i][j]
                yo = yo + yo_p
                print('yo',yo)
            yo_0 = activation(yo + self.bias[2][i])
            y_output.append(yo_0)
            print(y_output)

    def backward(self, error):

    def update_weights(self, lr = 0.1):

    # private functions
    def __calculate_total_net_input(self):

    # Apply the sigmoid activation function
    def __sigmoid(self, total_net_input):
        return 1/(1 + math.exp(-x))

    # Apply the node delta function
    def __node_delta(self, error):

class NeuronLayer:
    def __init__(self, weights_arr, bias_vec):
        self.weights_arr = weights_arr
        self.bias_vec = bias_vec

    # print the structure of the current neuron layer
    def inspect(self):
        print('Current NeuronLayer :')
        print('Neurons :', len(self.weights_arrs[0]))
        for j in range(0, len(self.weights_arrs[0])):
            print('Neuron ', j)
            for i in range(0, len(self.weights_arrs[0][j])):
                print('Weight :', self.weights_arrs[0][j][i])
            print('bias :', self.bias_vec[0][j])

    def feed_forward(self, inputs):

    # feed the node deltas of the current layer to the previous one
    def feed_backward(self, errors):

    # errors = layer_deltas for hidden layers
    def update_weights(self, lr = 0.1):

class NeuronNetwork:
    def __init__(self, weights_arrs, bias_arr):
        self.weights_arrs = weights_arrs
        self.bias_arr = bias_arr

    # weights_arrs is a 3D array, and bias_arr is a 2D array
    def inspect(self):
        print('Layers :', len(self.weights_arrs))
        print('NeuronLayer 0')
        print('Neurons :', len(self.weights_arrs[0]))
        for j in range(0, len(self.weights_arrs[0])):
            print('Neuron ', j)
            for i in range(0, len(self.weights_arrs[0][j])):
                print('Weight :', self.weights_arrs[0][j][i])
            print('bias :', self.bias_arr[0][j])
        print('NeuronLayer 1')
        print('Neurons :', len(self.weights_arrs[1]))
        for j in range(0, len(self.weights_arrs[1])):
            print('Neuron ', j)
            for i in range(0, len(self.weights_arrs[1][j])):
                print('Weight :', self.weights_arrs[1][j][i])
            print('bias :', self.bias_arr[1][j])
        print('NeuronLayer 2')
        print('Neurons :', len(self.weights_arrs[2]))
        for j in range(0, len(self.weights_arrs[2])):
            print('Neuron ', j)
            for i in range(0, len(self.weights_arrs[2][j])):
                print('Weight :', self.weights_arrs[2][j][i])
            print('bias :', self.bias_arr[2][j])

    def feed_forward(self, inputs):

    def compute_loss(self, training_inputs, training_outputs):

    # Uses online learning, ie updating the weights after each training epoch
    def train(self, training_inputs, training_outputs, lr = 0.1):        
        i1 = training_inputs[0]
        i2 = training_inputs[1]
        i3 = training_inputs[2]
        yd = training_outputs  

    ## private functions
    def __update_weights(self, lr = 0.1):

