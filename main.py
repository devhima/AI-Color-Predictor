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

# Importing NeuralNetwork class from classes
from neural_network import NeuralNetwork
from numpy import array

if __name__ == "__main__":

    print "Generating random starting synaptic weights: "

    #Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    # Printing generated weights
    print neural_network.synaptic_weights

    # The training set. We have 4 examples, each consisting of 4 input values & the first input is bias=1
    # and 1 output value.
    training_set_inputs = array([[1, 255, 0, 0], [1, 248, 80, 68], [1, 0, 0, 255], [1, 67, 15, 210]])
    training_set_outputs = array([[-1, -1, 1, 1]]).T
    
    print "Start training the neural network using a training set, about 10,000 times of training ... "
    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print "New synaptic weights after training: "
    print neural_network.synaptic_weights

    # Test the neural network with a new situation.
    print "Enter a new color values in RGB, and I'll predict if your color nearby red or blue:"
    r=eval(raw_input("R = "))
    g=eval(raw_input("G = "))
    b=eval(raw_input("B = "))
    print "Considering new situation [{}, {}, {}] -> ?: ".format(r,g,b)
    out = neural_network.think(array([1, r, g, b]))
    if out == 1:
    	print "I predict that your color is nearby blue (+1)"
    elif out == -1:
    	print "I predict that your color is nearby red (-1)"
