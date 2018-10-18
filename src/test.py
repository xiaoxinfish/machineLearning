import stockPreProcess as spp

sd = spp.stock()
sd.read('000016', 'stockData/000016_20181018.txt')
sd.print()
