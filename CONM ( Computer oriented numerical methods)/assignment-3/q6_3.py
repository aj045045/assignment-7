# Differential equation y' = y - x^2
def f(x, y):
    return y - x**2

# Milne's Predictor formula
def milne_predictor(y0, y1, y2, y3, f0, f1, f2, f3, h):
    return y0 + (4 * h / 3) * (2 * f3 - f2 + 2 * f1)

# Milne's Corrector formula
def milne_corrector(y2, y3, f2, f3, f_pred, h):
    return y2 + (h / 3) * (f_pred + 4 * f3 + f2)

# Given values for x and y
x_values = [0.0, 0.2, 0.4, 0.6]
y_values = [1, 1.12186, 1.46820, 1.7359]
h = 0.2  # Step size

# Compute f(x, y) for each known point
f_values = [f(x_values[i], y_values[i]) for i in range(4)]

# Milne's Predictor: Predict y(0.8)
y_pred = milne_predictor(y_values[0], y_values[1], y_values[2], y_values[3], 
                            f_values[0], f_values[1], f_values[2], f_values[3], h)

# Compute f(x=0.8, y_pred)
f_pred = f(0.8, y_pred)

# Milne's Corrector: Correct the predicted value
y_corr = milne_corrector(y_values[2], y_values[3], f_values[2], f_values[3], f_pred, h)

# Display results
print(f"Predicted value of y(0.8): {y_pred}")
print(f"Corrected value of y(0.8): {y_corr}")
