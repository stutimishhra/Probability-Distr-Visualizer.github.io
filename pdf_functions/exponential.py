import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

def exponential_pdf(lam):
    x = np.linspace(0, 15, 100)
    y = lam * np.exp(-lam * x)
    plt.plot(x, y, color='#30C3CD')
    plt.title('Exponential Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
