import numpy as np
import matplotlib.pyplot as plt

def uniform_pdf(a, b):
    x = np.linspace(a - 5, b + 5, 1000)
    y = np.where((x >= a) & (x <= b), 1 / (b - a), 0)
    plt.plot(x, y, color='#267C8F')
    plt.title('Uniform Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
