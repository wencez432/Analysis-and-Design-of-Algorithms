import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
import pandas as pd

def lineal(x,y):
    n = 24
    xm = np.mean(x)
    ym = np.mean(y)
    sum_xiyi = 0
    sum_xi2 = 0
    for i in range(n):
        sum_xiyi += (x[i] - xm) * (y[i] - ym)
        sum_xi2 += (x[i] - xm)**2
    b = sum_xiyi/sum_xi2
    a = ym - (b * xm)
    return a,b

ty = np.array([15.1564499,14.1557115,13.6790471,12.5457805,10.9156679,10.1238591,10.6217608,12.2922135,13.4015718,13.8156021,15.0960413,16.7179994,17.7324225,17.4625204,17.241814,18.0256319,17.3020026,16.4242477,16.3794495,17.4374239,15.627976,15.3852804,16.2911065,15.1442129])
x = np.array([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0,22.0,23.0])
plt.scatter(x,ty)


a,b = lineal(x,ty)
y_l = b + (a * x)
plt.plot(x,y_l)

plt.show()