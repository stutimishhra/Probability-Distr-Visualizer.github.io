import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

def gamma_pdf(shape, scale):
    x = np.linspace(0, 20, 100)
    y = gamma.pdf(x, shape, scale=scale)
    plt.plot(x, y, color='#30C3CD')
    plt.title('Gamma Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
