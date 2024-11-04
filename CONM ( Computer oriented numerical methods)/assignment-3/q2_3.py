import numpy as np

# Function to be integrated
def f(x):
    return 1 / (1 + x**2)

# Trapezoidal rule
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Simpson's 1/3 rule
def simpsons_one_third_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    
    for i in range(2, n - 1, 2):
        integral += 2 * f(a + i * h)
    
    integral *= h / 3
    return integral

# Simpson's 3/8 rule
def simpsons_three_eighth_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 3 * f(a + i * h)
    
    integral *= 3 * h / 8
    return integral

# Parameters
a = 0  # lower limit of integration
b = 6  # upper limit of integration
n = 6  # number of intervals

# Applying Trapezoidal rule
trap_result = trapezoidal_rule(f, a, b, n)
print(f"Trapezoidal rule result: {trap_result}")

# Applying Simpson's 1/3 rule
simpson_one_third_result = simpsons_one_third_rule(f, a, b, n)
print(f"Simpson's 1/3 rule result: {simpson_one_third_result}")

# Applying Simpson's 3/8 rule
# Note: For Simpson's 3/8 rule, n must be a multiple of 3.
if n % 3 == 0:
    simpson_three_eighth_result = simpsons_three_eighth_rule(f, a, b, n)
    print(f"Simpson's 3/8 rule result: {simpson_three_eighth_result}")
else:
    print(f"Simpson's 3/8 rule requires n to be a multiple of 3, but n={n} is not valid.")
