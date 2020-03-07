# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:26:09 2020

@author: wangl
"""

import numpy as np
import matplotlib.pyplot as plt

plt.subplot2grid((3, 3), (0, 0), colspan = 3)
plt.subplot2grid((3, 3), (1, 0), colspan = 2)
plt.subplot2grid((3, 3), (1, 2), rowspan = 2)
plt.subplot2grid((3, 3), (2, 0))
plt.subplot2grid((3, 3), (2, 1))

plt.savefig('sample7', dpi = 600)
plt.show()