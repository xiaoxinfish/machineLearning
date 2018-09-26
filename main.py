from simpleLinearRegression import SimpleLinearRegression as SimpleLR
import numpy as np

if __name__ == '__main__':
    xSet = np.array([1, 2, 2.5, 3, 5])
    ySet = np.array([2, 3.3, 4, 4.9, 6])
    sLR = SimpleLR(xSet, ySet, 3.2)
    sLR.predict()
    sLR.info()
    sLR.show()

