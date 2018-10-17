#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow as tf
import numpy as np
print('hello')


# # Reading data

# In[ ]:


timesteps = seq_length = 7
data_dim = 5
output_dim =1


# In[ ]:


# Open,High,Low,Close,Volume
xy = np.loadtxt('data-02-stock_daily.csv', delimiter = ',')
xy = xy[::-1] #reverse order (chronically ordered)
xy = MinMaxScaler(xy)
x = xy
y = xy[:, [-1]] #close as label

dataX = []
dataY = []
for i in range(0, len(y), - seq_length):
    _x = x[i:i + seq_length]
    _y = y[i + seq_length]
    print(_x, "->", _y)
    dataX.append(_x)
    dataY.append(_y)


# # Training and test datasets

# In[ ]:


# split to train and testing
train_size = int(len(dataY) * 0.7)
test_size = len(data_Y) - train_size
trainX, testX = np.array(dataX[0:train_size]),
                np.array(dataX[train_size:len(dataX)])
trainX, testX = np.array(dataY[0:train_size]),
                np.array(dataY[train_size:len(dataY)])
#input placeholders
X = tf.placeholder(tf.float32, [None, seq_length, data_dim])
Y = tf.placeholder(tf.float32, [None, 1 ])


# # LSTM and Loss

# In[ ]:


# input placeholders
X = tf.placeholder(tf.float32, [None, seq_length, data_dim])
Y = tf.placeholder(tf.float32, [None,1])

cell = tf.contrib.rnn.BasicLSTMCell(num_units = output_dim, state_is_tuple = True)
outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype - tf.float32)
Y_pred = outputs[:, -1] #we use the last cell's output

#cost/lost
loss = tf.reduce_sum(tf.square(Y_pred -Y)) # sum of the squares
#optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


# # Training and Results

# In[ ]:


sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    _, l = sess.run([train, loss]),
        feed_dict = {X: trainX, Y: trainY})
    print(i, l)

testPredict = sess.run(Y_pred, fee_dict = {X: testX})

plt.plot(testY)
plt.plot(testPredict)
plt.show()

