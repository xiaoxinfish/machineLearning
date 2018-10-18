import re
class stock:
    def __init__(self):
        self.stockSet = {}

    def read(self, stockCode, dataFile):
        with open(dataFile, 'r') as fo:
            dailyData = {}
            for line in fo.readlines():
                data = re.split(r'\s+', line)
                if re.match(r'\d{4}/\d{1,2}/\d{1,2}',data[1]):
                    dailyData[data[1]] = [data[2], data[3], data[4], data[5], data[6]]
            self.stockSet[stockCode] = dailyData

    def print(self):
        for stockCode, dailyDataSet in self.stockSet.items():
            for day, value in dailyDataSet.items():
                print('{} {} {}'.format(stockCode, day, value))




