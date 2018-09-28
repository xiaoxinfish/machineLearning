import numpy as np
import matplotlib.pyplot as plt

class SimpleLinearRegression:
    def __init__(self, sample_XCordinate, sample__YCordinate, x):
        self.xSet_ = sample_XCordinate
        self.ySet_ = sample__YCordinate
        self.a_ = 0
        self.b_ = 0
        self.x_ = x
        self.yPredict_ = 0

    def predict(self):
        x_mean = np.mean(self.xSet_)
        y_mean = np.mean(self.ySet_)
        num1 = 0
        num2 = 0
        for i in range(len(self.xSet_)):
            num1 += (self.xSet_[i] - x_mean) * (self.ySet_[i] - y_mean)
            num2 += (self.xSet_[i] - x_mean) ** 2
        self.a_ = num1 / num2
        self.b_ = y_mean - x_mean * self.a_
        self.yPredict_ = self.a_ * self.x_ + self.b_
        return self.yPredict_

    def info(self):
        print(" y = {} * x + {}".format(self.a_, self.b_))
        
    def show(self):
        plt.scatter(self.xSet_, self.ySet_)
        y_new = self.a_ * self.xSet_ + self.b_
        plt.plot(self.xSet_, y_new, 'r')
        plt.scatter(self.x_, self.yPredict_, c='y')
        plt.show()
