import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

def hypergeometric_pdf(M, n, N):
    x = np.arange(0, N+1)
    y = hypergeom.pmf(x, M, n, N)
    plt.plot(x, y, color='#30C3CD')
    plt.title('Hypergeometric Distribution PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    return x, y
