# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:46:57 2020

@author: wangl
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'FangSong'
matplotlib.rcParams['font.size'] = 20

a = np.arange(0.0, 5.0, 0.02)
plt.xlabel("X轴：时间")
plt.ylabel("Y轴：振幅")

plt.plot(a, np.cos(2 * np.pi * a) + 1, 'g--')
plt.savefig('sample4', dpi = 600)
plt.show()