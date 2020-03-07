# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:58:50 2020

@author: wangl
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0, 5.0, 0.02)
plt.xlabel("X轴：时间", fontproperties = "FangSong", fontsize = 20)
plt.ylabel("Y轴：振幅", fontproperties = "FangSong", fontsize = 20)

plt.plot(a, np.cos(2 * np.pi * a) + 1, 'r--')
plt.savefig('sample5', dpi = 600)
plt.show()