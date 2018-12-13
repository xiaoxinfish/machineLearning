代码调试成功。
但是：
1>原代码中，交易数据，在x轴，也就是时间序列上，被倒置了。导致，绘图时，图形是x轴反向的。目前代码，去除了倒置。不知道为什么要倒置。
2>输出实际收盘价与预测收盘价时，预测值，在图上，延迟一天。目前代码，强制对齐。不知道这个延迟，到底时代表什么。目前的猜想，并没有真正延迟一天，
  而是，前一天的值，对预测值影响的权重最大，所以预测值，会拟合前一天的值，看上去，就好像延迟1天一样。
3>Y_pred = outputs[:, -1] #we use the last cell's output 不明白，为什么用cell里的最后一个，作为Y predict


baidu "数学烂也要学AI"
张量

pip install --upgrade --ignore-installed -i http://pypi.douban.com/simple/
