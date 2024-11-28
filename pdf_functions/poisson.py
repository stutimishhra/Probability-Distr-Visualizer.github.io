import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def poisson_pdf(lam):
    x = np.arange(0, 15)
    y = poisson.pmf(x, lam)
    plt.plot(x, y, color='#267C8F')
    plt.title('Poisson Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
