import tensorflow as tf
import numpy as np

# define model architecture
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
# compile the model  
model.compile(optimizer='sgd',loss='mean_squared_error')
# define training data
xs = np.array([-1.0,0.0,1.0,2.0,3.0,4.0],dtype = float)
ys = np.array([-3.0,-1.0,1.0,3.0,5.0,7.0],dtype = float)
# train the model
model.fit(xs,ys,epochs=500)
# make prediction
print(model.predict([10.0]))   # output == 19