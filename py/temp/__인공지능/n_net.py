import math
import numpy as np
import random as rd

def sigmoid(x):
    return 1 / (1 + math.e**-x)

def ReLU(x):
    return max(0, x)

def soft_max(X):
    X = np.array(X)
    tmp = list(map(lambda x: math.e**x, X))
    tot = sum(tmp)
    Y = np.array(list(map(lambda x: (math.e**x)/tot, X)))

    return Y

class model:
    active = ReLU#sigmoid
    
    def __init__(self, size): # ex) [784, 100, 10]
        for n in size:
            if n <= 0:
                raise Exception('Incorrect design')
        self.size = size
        self.layers = [np.array([0]*n) for n in size]
        
        self.output = np.array([0]*size[-1])

        self.weights = [] # 2차원 np배열들이 들어간다. 3차원이 된다.
        self.biases = [] # 1차원 np배열들이 들어간다. 2차원이 된다.
    
        self.Z_layers = [np.array([0]*n) for n in size[1:]] # 미분때 필요

        self.del_layers = [np.array([0]*n) for n in size[1:]]
        self.d_weights = []
        self.d_biases = []

        self.set_weights()
        self.set_biases()

        self.costs = []
        self.sum_cost = None
        

    def set_weights(self):
        for i in range(len(self.size)-1):
            weight = np.random.randn(self.size[i+1], self.size[i])
            self.weights.append(weight)


    def set_biases(self):
        for n in self.size:
            bias = np.random.randn(n)
            self.biases.append(bias)
        del self.biases[0]


    def input(self, X):
        if len(X) != self.size[0]:
            raise Exception('No match input_langth')
        self.layers[0] = np.array(X)


    def compute(self, mode='test'):
        if mode == 'test':
            for i in range(len(self.layers)-1):
                X = self.layers[i]
                W = self.weights[i]
                B = self.biases[i]
                
                X = np.matrix(X).T
                W = np.matrix(W)
                B = np.matrix(B).T
                Y = W*X + B

                Y = Y.A.flatten() # .T 할 필요없이 납작하게
                self.Z_layers[i] = Y
                self.layers[i+1] = np.array(list(map(model.active, Y)))

            self.output = soft_max(self.layers[-1])

        elif mode == 'train':


    def batch_cel(self, batch_xs, batch_ys): # 
        for i in range(len(batch_xs)): # 기본 100개씩
            self.input(batch_xs[i])
            self.compute()
            self.add_cost(batch_ys[i])

        self.sum_cost = sum(self.costs)


    def add_cost(self, label):
        if len(label) != self.size[-1]:
            raise Exception('No match label ans output_layer')
        label = np.array(label)
        cost_line = (self.output - label)**2 # 오차들 # 제곱오차
        cost = sum(cost_line) / self.size[-1]

        self.costs.append(cost)

            
if __name__ == '__main__':
    l = [1,2,3,4,5]
    print(soft_max(l))
    







    
