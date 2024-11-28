import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

def negative_binomial_pdf(r, p):
    x = np.arange(0, 15)
    y = nbinom.pmf(x, r, p)
    plt.plot(x, y, color='#267C8F')
    plt.title('Negative Binomial Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
