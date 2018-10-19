import stockPreProcess as spp

sd = spp.stock()
sd.readOriginalData('000016', 'stockData/000016_20181018.txt')
sd.saveToCSV('000016')
