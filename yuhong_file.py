#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:40:56 2019

@author: ryanjeong
"""

import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt

dataPoint = input("Input data point for p-value calculation")
dataPoint = float (dataPoint)

# Generate some data for this demonstration.
# This is data for January, account 701.03
data = [177043.97, 125049.16, 92061.47, 59509.43, 46445.99, 31708.69, 28394.38, 22661.03]

# Fit a normal distribution to the data:
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='g')

# Plot the PDF.
# Find max and min limitations of x-axis
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Find the Gaussian curve
p = norm.pdf(x, mu, std)

#Plot the graph
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)

#Determining z-score, input into p-value expression.
z_score = (dataPoint - mu)/std

p_value = st.norm.sf(abs(z_score))*2

print(p_value)

plt.show()