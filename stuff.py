import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten


Xdata = np.load("data/geometric/data1_Xdata.npy")
xs = []
ys = []
for thing in Xdata:
    xs.append(thing[0])
    ys.append(thing[1])



thing, otherthing = kmeans(Xdata,3)
print(thing)
print(otherthing)
