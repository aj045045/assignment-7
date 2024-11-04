# Function for the differential equation y' = 1 - y
def f(x, y):
    return 1 - y

# Euler's method to find y-values at x = 0.1, 0.2, 0.3, 0.4
def euler_method(f, x0, y0, h, x_end):
    x_values = []
    y_values = []
    
    x = x0
    y = y0
    
    while x <= x_end:
        x_values.append(x)
        y_values.append(y)
        y = y + h * f(x, y)
        x = x + h
        
    return x_values, y_values

# Adams-Bashforth predictor-corrector method for y(0.5)
def adams_bashforth_predictor_corrector(f, x_values, y_values, h):
    n = len(x_values) - 1  # Last index of known values
    
    # Predictor step (Adams-Bashforth 2-step method)
    y_pred = y_values[n] + (h / 2) * (3 * f(x_values[n], y_values[n]) - f(x_values[n-1], y_values[n-1]))
    
    # Corrector step (Adams-Moulton method)
    y_corr = y_values[n] + (h / 2) * (f(x_values[n] + h, y_pred) + f(x_values[n], y_values[n]))
    
    return y_pred, y_corr

# Initial conditions
x0 = 0    # starting x-value
y0 = 0    # initial value of y at x = 0
h = 0.1   # step size
x_end = 0.4  # endpoint for Euler's method

# Step 1: Use Euler's method to compute values at x = 0.1, 0.2, 0.3, 0.4
x_values, y_values = euler_method(f, x0, y0, h, x_end)

# Tabulate results from Euler's method
print("x\t y (Euler)")
for i in range(len(x_values)):
    print(f"{x_values[i]:.1f}\t {y_values[i]:.6f}")

# Step 2: Use Adams-Bashforth method to find y(0.5)
y_pred, y_corr = adams_bashforth_predictor_corrector(f, x_values, y_values, h)

# Display predicted and corrected values for y(0.5)
print(f"\nPredicted value of y(0.5): {y_pred:.6f}")
print(f"Corrected value of y(0.5): {y_corr:.6f}")
