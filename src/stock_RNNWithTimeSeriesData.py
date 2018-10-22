#!/usr/bin/env python
# coding: utf-8
from logger import logger
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os.path
import time
import stockPreProcess as spp
from sklearn.preprocessing import minmax_scale

logger = logger()

print('hello world!')

# # Reading data

timesteps = seq_length = 7
data_dim = 5
output_dim =1
# get clear up data


stockCode = '000016'
originalFileName = 'stockData/000016_20181018.txt'
CSVFileName = 'stockData/' + stockCode + '_Daily_' + time.strftime('%Y-%m-%d', time.localtime(time.time()))  + '.csv'
sd = spp.stock()
sd.readOriginalData(stockCode, originalFileName)
sd.saveToCSV(stockCode, CSVFileName)

xy = np.loadtxt(CSVFileName, delimiter = ',')

'''
#为了绘图时，Y轴坐标系在同一范围内，要对原始收盘价，做适配
y_original = xy[:, [-1]] # y_original 原始收盘价
y_original_max = np.max(y_original)
y_original_adapter = [i / y_original_max for i in y_original]
print(y_original)
print(y_original_max)
print(y_original_adapter)
'''

#xy = xy[::-1] #reverse order (chronically ordered) #不清楚，为什么要倒置一下

logger.info(xy)
xy = minmax_scale(xy)

x = xy
y = xy[:, [-1]] #pick up the close price as label

dataX = []
dataY = []
for i in range(0, len(y) - seq_length):
    _x = x[i:i + seq_length]
    _y = y[i + seq_length]
    #print('{} -> {}'.format(_x, _y))
    logger.debug('{} -> {}'.format(_x, _y))
    dataX.append(_x)
    dataY.append(_y)

# # Training and test datasets

# split to train and testing
train_size = int(len(dataY) * 0.7)
test_size = len(dataY) - train_size
#print("test date size:{}".format(test_size))
logger.debug("test date size:{}".format(test_size))
trainX, testX = np.array(dataX[0:train_size]), np.array(dataX[train_size:len(dataX)])
trainY, testY = np.array(dataY[0:train_size]), np.array(dataY[train_size:len(dataY)])

#y_original_adapter = np.array(y_original_adapter[train_size:len(dataY)])

# # LSTM and Loss

# input placeholders
X = tf.placeholder(tf.float32, [None, seq_length, data_dim])
Y = tf.placeholder(tf.float32, [None, 1])

cell = tf.nn.rnn_cell.LSTMCell(name = 'basic_lstm_cell', num_units = output_dim, state_is_tuple = True)
outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype = tf.float32)
Y_pred = outputs[:, -1] #we use the last cell's output

#cost/lost
loss = tf.reduce_sum(tf.square(Y_pred -Y)) # sum of the squares
#optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


# # Training and Results


sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    _, l = sess.run([train, loss], feed_dict = {X: trainX, Y: trainY})
    #print(i, l)
    logger.debug('{}, {}'.format(i, l))

testPredict = sess.run(Y_pred, feed_dict = {X: testX})
plt.plot(testY, 'r')
plt.plot(testPredict, 'b')
total = 0
for i in range(len(testY)-1):
    delta = abs((testPredict[i+1] - testY[i]) * 100 / testY[i])
    total += delta
    print('test:{} predict:{} delta:{}%'.format(testY[i], testPredict[i+1], delta))
print('average delta:{}%'.format(total/(len(testY)-1)))
#plt.plot(testPredict[1:], 'b') #发现图形上，testY比testPredict提前了一天。为什么？？？？
#plt.plot(y_original_adapter[7:], 'g') #预测值在x坐标上，与实际收盘价，差7天（seq_length)
plt.show()



