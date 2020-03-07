# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:40:14 2020

@author: wangl
"""

import numpy as np
import matplotlib.pylab as plt

fig, ax = plt.subplots()
ax.plot(10 * np.random.random(100), 10 * np.random.randn(100), 'o')
ax.set_title("sample12")

plt.savefig("sample12", dip = 600)
plt.show()