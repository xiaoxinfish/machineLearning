import re

class stock:
    def __init__(self):
        self.stockSet = {}

    def readOriginalData(self, stockCode, fileName):
        with open(fileName, 'r') as fr:
            dailyData = {}
            for line in fr.readlines():
                data = re.split(r'\s+', line)
                tradeTime = data[1]
                if re.match(r'\d{4}/\d{1,2}/\d{1,2}', tradeTime):
                    priceOpen = data[2]
                    priceHigh = data[3]
                    priceLow = data[4]
                    priceClose = data[5]
                    vol = int(data[6]) / 10000
                    dailyData[tradeTime] = [priceOpen, priceHigh, priceLow, priceClose, vol]
            self.stockSet[stockCode] = dailyData

    def print(self):
        for stockCode, dailyDataSet in self.stockSet.items():
            for day, value in dailyDataSet.items():
                print('{} {} {}'.format(stockCode, day, value))

    def saveToCSV(self, stockCode, fileName):
        with open(fileName, 'w') as fw:
            for key, value in self.stockSet[stockCode].items():
                fw.write('{},{},{},{},{}\n'.format(value[0], value[1], value[2], value[4], value[3]))




