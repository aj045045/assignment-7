# Function for the differential equation y' = x + y
def f(x, y):
    return x + y

# Runge-Kutta 4th order method
def rk4(f, x0, y0, h, x_end):
    x = x0
    y = y0
    
    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h
        print(f"Approximate value of y({round(x,2)}) using 4th order RK method: {y:4f}")

# Initial conditions and step size
x0 = 0     # starting x-value
y0 = 1     # initial value of y at x = 0 (assume y(0) = 1)
h = 0.1    # step size
x_end = 0.4 # endpoint of the interval

rk4(f, x0, y0, h, x_end)

