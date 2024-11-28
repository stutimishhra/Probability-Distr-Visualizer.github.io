import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def binomial_pdf(n, p):
    x = np.arange(0, n+1)
    y = binom.pmf(x, n, p)
    plt.plot(x, y, color='#30C3CD')
    plt.title('Binomial Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
