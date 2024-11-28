import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

def geometric_pdf(p):
    x = np.arange(1, 11)
    y = geom.pmf(x, p)
    plt.plot(x, y, color='#30C3CD')
    plt.title('Geometric Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
