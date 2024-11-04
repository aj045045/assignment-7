# Function for the derivative y' = 1 + y^2
def f(y):
    return 1 + y**2

# Euler's method implementation
def euler_method(f, x0, y0, h, x_end):
    x = x0
    y = y0
    while x != x_end:
        y = y + h * f(y)
        x = x + h
    y = y + h * f(y)
    return y

# Initial condition
x0 = 0      # starting x-value
y0 = 0      # initial value of y at x = 0
h = 0.2     # step size
x_end = 0.8 # we want to find y(0.8)

# Solving the ODE using Euler's method
y_at_08 = euler_method(f, x0, y0, h, x_end)

# Display the result
print(f"Approximate value of y(0.8) using Euler's method: {y_at_08}")
