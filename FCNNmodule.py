from scipy.linalg import norm
import numpy as np
import math

class Neuron:
    def __init__(self, weights_vec, bias):
        self.weights_vec = weights_vec
        self.bias = bias

    def forward(self, inputs):
        activation = self.__sigmoid 
        self.inputs = inputs        
        self.output = activation(self.__calculate_total_net_input())        
        return self.output
        # self.error = 0.5 * (target_output - self.output) ** 2

    def backward(self, error):       
        pd_total_output = 0
        for i in range(0, len(self.weights_vec)):

            pd_total_output +=self.__node_delta(error[i]) * self.weights_vec[i]
        self.delta = pd_total_output * self.output * (1 - self.output) * self.inputs
        return self.delta

    def update_weights(self, lr = 0.1):
        for i in range(0, len(self.weights_vec)):
            self.weights_vec[i] = self.weights_vec[i] - lr * self.delta

    # private functions
    def __calculate_total_net_input(self):
        total = 0
        for i in range(0, len(self.inputs)):
            total += self.inputs[i] * self.weights_vec[i]            
        return total + self.bias

    # Apply the sigmoid activation function
    def __sigmoid(self, total_net_input):
        return 1/(1 + math.exp(-total_net_input))

    # Apply the node delta function
    def __node_delta(self, error):
        return -error * self.output(1 - self.output)

class NeuronLayer:
    def __init__(self, weights_arr, bias_vec):
        self.weights_arr = weights_arr
        self.bias_vec = bias_vec
        self.outputlayer = []
        # print the structure of the current neuron layer
    def inspect(self):
        # print('Current NeuronLayer :')
        for j in range(0, len(self.weights_arr)):
            print('Neuron ', j)
            for i in range(0, len(self.weights_arr[j])):
                print('Weight :', self.weights_arr[j][i])
            print('bias :', self.bias_vec[j])
        

    def feed_forward(self, inputs):        
        for i in range(0, len(self.weights_arr)):
            N = Neuron(self.weights_arr[i], self.bias_vec[i])            
            self.outputlayer.append(N.forward(inputs))      
        # print('NeuronLayer', self.outputlayer)        
        return self.outputlayer        

    # feed the node deltas of the current layer to the previous one
    def feed_backward(self, errors):
        self.deltalayer = []
        for i in range(0, len(self.weights_arr)):

            # self.deltalayer.append(N.backward(errors[i]))
            print(self.outputlayer)
        return self.deltalayer
    # errors = layer_deltas for hidden layers
    # def update_weights(self, lr = 0.1):
        


class NeuronNetwork:
    def __init__(self, weights_arrs, bias_arr):
        self.weights_arrs = weights_arrs
        self.bias_arr = bias_arr
        self.outputnetwork = []
        self.errors = []

    # weights_arrs is a 3D array, and bias_arr is a 2D array
    def inspect(self):
        print('Layers :', len(self.weights_arrs))
        for i in range(0, len(self.weights_arrs)):
            print('NeuronLayer', i)
            N_inspect = NeuronLayer(self.weights_arrs[i], self.bias_arr[i])
            N_inspect.inspect()


    def feed_forward(self, inputs):        
        self.output = []
        #intput layer        
        N_intput = NeuronLayer(self.weights_arrs[0], self.bias_arr[0])                 
        self.output.append(N_intput.feed_forward(inputs))
        # print('intput layer', self.outputnetwork)       
        # print('input done')  
        #hidden layer
        for i in range(1, len(self.weights_arrs)):            
            N_hidden = NeuronLayer(self.weights_arrs[i], self.bias_arr[i])            
            self.output.append(N_hidden.feed_forward(self.output[i-1]))          
        self.outputnetwork.append(self.output)  
        # print('outputs', self.outputnetwork) 
        return self.output

    def compute_loss(self, training_inputs, training_outputs):
        #error
        for i in range(0, len(training_inputs)):
            # print('input', training_inputs[i])
            self.feed_forward(training_inputs[i])
            output = self.output[len(self.weights_arrs)-1][0]
            self.errors.append(training_outputs[i] - output)            
            print('errors', self.errors)

    # Uses online learning, ie updating the weights after each training epoch
    def train(self, training_inputs, training_outputs, lr = 0.1):        
        i1 = training_inputs[0]
        i2 = training_inputs[1]
        i3 = training_inputs[2]
        yd = training_outputs  

    ## private functions
    def __update_weights(self, lr = 0.1):
        i = 0



## Test of FCNN creation
weights_arrs = [[[0.1,0.2,0.3],[0.4,0.5,0.6],[0.7,0.8,0.9]], # init weights of the 1st neuron layer
[[1.1,1.2,1.3],[1.4,1.5,1.6],[1.7,1.8,1.9],[1.3, 1.2, 1.1]], # init weights of the 2nd neuron layer
[[2.1,2.2,2.3,2.4]]] # init weights of the 3rd neuron layer
bias_arr = [[0.1,0.2,0.3], # init biases of the 1st neuron layer
[1.1,1.2,1.3,1.4], # init biases of the 2nd neuron layer
[2.1]] # init biases of the 3rd neuron layer
# nn = NeuronNetwork(weights_arrs, bias_arr)
# nn.inspect()
inputs = [[0, 1, 0], [1, 1, 1], [1, 0, 0], [0, 0, 1]]
training_inputs = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
training_outputs = [0, 1, 1, 0, 1, 0, 0, 1]
nn = NeuronNetwork(weights_arrs, bias_arr)
# nn.feed_forward(inputs)
# nn.inspect()
nn.compute_loss(training_inputs, training_outputs)