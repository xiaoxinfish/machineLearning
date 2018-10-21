import stockPreProcess as spp
import numpy as np

def convStockDataToCSV():
    sd = spp.stock()
    sd.readOriginalData('000016', 'stockData/000016_20181018.txt')
    sd.saveToCSV('000016')

def arrayAppend():
    y = [1.2,3.1,4.5,5.1,6.1]
    print(y)
    y = y[2:]
    print(y)

if __name__ == '__main__':
    arrayAppend()
