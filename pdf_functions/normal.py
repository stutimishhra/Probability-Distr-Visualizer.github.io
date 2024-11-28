import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def normal_pdf(mu, sigma):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    y = norm.pdf(x, mu, sigma)
    plt.plot(x, y, color='#267C8F')
    plt.title('Normal Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
