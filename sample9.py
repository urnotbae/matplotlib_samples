# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:48:52 2020

@author: wangl
"""
import matplotlib.pyplot as plt

labels = "Python", "Java", "C/C++", "C#", "Javascript", "Other"
sizes = [31.2, 19.6, 15.9, 7.4, 3.6, 22.3]
explode = [0.1, 0, 0, 0, 0, 0]
plt.pie(sizes, explode = explode, labels = labels, autopct = "%.2f%%",\
        shadow = False, startangle = 90)
plt.title(r'2015最受欢迎的编程语言', fontproperties = "SimHei", fontsize = 20)
#plt.axis('equal')

plt.savefig("sample9", dpi = 600)
plt.show()