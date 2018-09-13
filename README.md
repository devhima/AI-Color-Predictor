# AI-Color-Predictor

AI Color Predictor - By. Ibrahim Said Elsharawy (www.devhima.tk)

This project is a single layer neural network consists of 4 inputs __4 neurons__ (first is bias=1 & others is RGB color values) and one output __1 neuron__

This neural net trains itself on 4 samples of (RGB) red & blue colors using signum & signum_derivative & dirac_delta functions to classify your inputed color to blue +1 or red -1

Here is the mathematical representation of the idea: 

- Trainning data samples & Neural Network:

![math1](https://github.com/devhima/AI-Color-Predictor/raw/master/images/math1.jpg)

- Calculation of the output Y with signum function:

![math2](https://github.com/devhima/AI-Color-Predictor/raw/master/images/math2.jpg)

- The weight adaptation steps:

![math2](https://github.com/devhima/AI-Color-Predictor/raw/master/images/math3.jpg)

Screenshot of some tests:

![screen1](https://github.com/devhima/AI-Color-Predictor/raw/master/images/screen01.jpg)

![screen2](https://github.com/devhima/AI-Color-Predictor/raw/master/images/screen02.jpg)
