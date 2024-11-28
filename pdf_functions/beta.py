import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def beta_pdf(a, b):
    x = np.linspace(0, 1, 100)
    y = beta.pdf(x, a, b)
    plt.plot(x, y, color='#267C8F')
    plt.title('Beta Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
