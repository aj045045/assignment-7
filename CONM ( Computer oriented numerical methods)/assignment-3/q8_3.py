# Define the data points
x = [0, 1, 2, 3, 4]
y = [1, 2.718, 7.381, 20.86, 54.598]

# Calculate the derivative f'(0) using forward difference
f_prime_at_0 = (y[1] - y[0]) / (x[1] - x[0])

# Print the result
print(f"f'(0) = {f_prime_at_0:.3f}")
