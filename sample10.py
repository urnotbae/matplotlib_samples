# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:12:21 2020

@author: wangl
"""

import numpy as np
import matplotlib.pylab as plt
 
np.random.seed(0)
mu, sigma = 0, 1
a = np.random.normal(mu, sigma, size=10000)

fig, ax = plt.subplots()
ax.hist(a, bins = 100, density = True, facecolor = 'b', alpha=0.5)
plt.title(r"直方图", fontproperties = "SimHei", fontsize = 20)
x = np.linspace(-5, 5, 1000)
ax.plot(x, 1 / np.sqrt(2*np.pi) * np.exp(-(x**2)/2), linewidth=2)

plt.savefig("sample10", dpi = 600)
plt.show()