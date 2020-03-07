# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:23:15 2020

@author: wangl
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
a = np.arange(10)
plt.plot(a, 1.5 * a, 'go-', a, 3.5 * a, 'rx', a, a*a, 'b*:')
plt.axis([0, 10, 0, 100])
plt.ylabel('Y轴')

plt.savefig('sample3', dpi = 600)
plt.show()