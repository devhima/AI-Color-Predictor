'''
AI Color Predictor - By. Ibrahim Said Elsharawy (www.devhima.tk)
This project is a single layer neural network consists of
4 inputs __4 neurons__ (first is bias=1 & others is RGB color values)
and one output __1 neuron__
this neural net trains itself on 4 samples of (RGB) red & blue colors
using signum & signum_derivative & dirac_delta functions
to classify your inputed color to blue +1 or red -1
'''

'''
MIT License

Copyright (c) 2018 Ibrahim Said Elsharawy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from numpy import array, random, dot
import copy

class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(1)

        # We model a single neuron, with 4 input connections (3 inputs & bias) and 1 output connection.
        # We assign random weights to a 4 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synaptic_weights = 2 * random.random((4, 1)) - 1

    # The signum function, which extracts the sign of a real number x
    # We pass the weighted sum of the inputs through this function to
    # normalise them between -1 and +1.
    def __signum(self, x):
        return x / abs(x)

# Dirac delta function to calculate the
# derivative of the signum function.
    def __dirac_delta(self, x, eps, infinite):
    	y=copy.deepcopy(x)
    	for i in range(y.size):
    		if (x[i]>=-eps and x[i]<=eps and x[i]!=0):
    			y[i]=[infinite]
    		else:
    			y[i]=[0]
    	return y

    # The derivative of the signum function.
    # It indicates how confident we are about the existing weight.
    # It returns 1 or 0
    def __signum_derivative(self, x):
    	y = 2 * self.__dirac_delta(x,1,0.5)
        return y

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # Pass the training set through our neural network (a single neuron).
            output = self.think(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            error = training_set_outputs - output

            # Multiply the error by the input and again by the derivative of the signum function.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T, error * self.__signum_derivative(output))

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # The neural network thinks.
    def think(self, inputs):
        # Pass inputs through our neural network (to our output single neuron).
        return self.__signum(dot(inputs, self.synaptic_weights))
