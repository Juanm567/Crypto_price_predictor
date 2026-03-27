import tensorflow as tf 
import numpy as np 
Sequential = tf.keras.models.Sequential # Sequential is a linear stack of layers, tried to import on heading but it was being annoying
simpleRNN = tf.keras.layers.SimpleRNN   # the reccurent neural network layer, which is used to process sequential data
Dense = tf.keras.layers.Dense           #every neuron in the layer is connected to every neuron in the previous layer, giving us the result 
#mock data set
data = np.array([1,2,3,4,5,6,7,8,9])
x = [] 
y = [] 
for i in range(len(data)-3):
    x.append(data[i:i+3])
    y.append(data[i+3]) #training model on 4th element
new_x = []              #new data array with only 3 elements
for i in x:
    if len(i) == 3:
        new_x.append(i)
new_x = np.array(new_x)
new_y = np.array(y)
#reshaping data to fit the model. x.shape = (7,3) 7 rows and 3 columns, 1 feature (variable) -> what the RNN expects as input
new_x = new_x.reshape((new_x.shape[0], new_x.shape[1], 1))#x.shape[0] = 7, x.shape[1] = 3, 1 feature (variable) 
#building the model
model = Sequential([
    simpleRNN(units = 60, activation = 'relu'),
    Dense(units = 1)
])
#compile the model
model.compile(optimizer = 'adam', loss = 'mse')                 #algorithm adam used to update weights, mse is used as a loss function to evaluate the performance of the model
model.fit(new_x, new_y, epochs = 400)                           #(epoch)ammount of times to apply and evaluate the activator function 'reLU'
x =(model.predict(np.array([[7,8,9]]).reshape(1,3,1)))          #array to predict and reshape to fit the model
print(int(x.item()))





