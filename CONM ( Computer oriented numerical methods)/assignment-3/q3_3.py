import numpy as np

# Function to be integrated
def f(x):
    return 1 / (1 + x**2)

# Gauss-Legendre Quadrature for n = 2
def gauss_legendre_n2(f):
    # Nodes and weights for n = 2
    x1 = -1 / np.sqrt(3)
    x2 = 1 / np.sqrt(3)
    w1 = 1
    w2 = 1

    # Gauss quadrature formula
    integral = w1 * f(x1) + w2 * f(x2)
    return integral

# Gauss-Legendre Quadrature for n = 3
def gauss_legendre_n3(f):
    # Nodes and weights for n = 3
    x1 = -np.sqrt(3/5)
    x2 = 0
    x3 = np.sqrt(3/5)
    
    w1 = 5 / 9
    w2 = 8 / 9
    w3 = 5 / 9

    # Gauss quadrature formula
    integral = w1 * f(x1) + w2 * f(x2) + w3 * f(x3)
    return integral

# Evaluate the integral using Gauss-Legendre quadrature for n = 2 and n = 3
integral_n2 = gauss_legendre_n2(f)
integral_n3 = gauss_legendre_n3(f)

# Display the results
print(f"Gauss-Legendre Quadrature result for n=2: {integral_n2}")
print(f"Gauss-Legendre Quadrature result for n=3: {integral_n3}")
