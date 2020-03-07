# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:01:11 2020

@author: wangl
"""

import numpy as np
import matplotlib.pyplot as plt
 
a = np.arange(0.0, 10.0, 0.1)
plt.plot(a, np.cos(a * np.pi) + 2, 'r--')
 
plt.xlabel("X轴: 时间", fontproperties="FangSong", fontsize=15, color='green')
plt.ylabel("Y轴: 振幅", fontproperties="FangSong", fontsize=15)
plt.title(r'正弦波实例$y=cos(\pi x)$', fontproperties="SimHei", fontsize=20)
plt.text(2, 3, r'$\mu=?$', fontsize=15)
plt.annotate(r'this', xy = (7, 1), xytext = (9.5, 0.5), arrowprops = dict(facecolor = "green", shrink = 0.1, width = 2)) 

plt.axis([-1, 12, 0, 4])
plt.grid(True)
plt.savefig('sample6', dpi=600)
plt.show()