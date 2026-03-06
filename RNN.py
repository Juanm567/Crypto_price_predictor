import tensorflow as tf #importing tensorflow library for training and deploying deep neural networks
import numpy as np # We need numpy so that we can cleand ata and make it ready fot tensorflows tensor format
Sequential = tf.keras.models.Sequential # Sequential is a linear stack of layers, tried to import on heading but it was being annoying
simpleRNN = tf.keras.layers.SimpleRNN # the reccurent neural network layer, which is used to process sequential data
Dense = tf.keras.layers.Dense #every neuron in the layer is connected to every neuron in the previous layer, giving us the result 

data = np.array([1,2,3,4,5,6,7,8,9,10]) #our data which is a simple 1-10 sequence
x = [] #empty list to store our input sequences
y = [] #empty list to store our output sequences
seq_len = 3 #the length of the input sequence we want to use for training
#model looks at the past 3 numbers to predict the 4th one
