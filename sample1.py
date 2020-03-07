# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:45:42 2020

@author: wangl
"""

import matplotlib.pyplot as plt

plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
plt.ylabel('Y')
plt.axis([0, 10, 0, 8])
plt.savefig('sample1', dpi = 600)
plt.show()