#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

#data
x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

#plot
plt.plot(x, y, c='blue')
plt.xscale('linear')
plt.xlim(0, 28650)
plt.yscale('log')
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponetial Decay of C-14')
plt.show()
