import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

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
# Find the guassian curve
p = norm.pdf(x, mu, std)
#Plot the graph
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)

plt.show()