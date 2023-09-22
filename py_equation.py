import matplotlib.pyplot as plt
import numpy as np

# Linear Equation: y = mx + b
def linear_equation(x):
    m = 2  # Slope
    b = -12  # Y-intercept
    return m * x + b

# Quadratic Equation: y = ax^2 + bx + c
def quadratic_equation(x):
    a = 1  # Coefficient of x^2
    b = 8  # Coefficient of x
    c = 15  # Constant term
    return a * x**2 + b * x + c

# Quadratic Equation: y = ax^2 + bx + c
def quadratic_equation_inv(x):
    a = 1  # Coefficient of x^2
    b = 8  # Coefficient of x
    c = -15  # Constant term
    return a * x**2 + b * x + c

# Generate x values
x = np.linspace(-5, 5, 100)  # Creating 100 evenly spaced points between -5 and 5

# Calculate y values for both linear and quadratic equations
y_linear = linear_equation(x)
y_quadratic = quadratic_equation(x)
y_quadratic_inv = quadratic_equation_inv(x)

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the linear equation
plt.subplot(1, 2, 1)
plt.plot(x, y_linear, label='y = 2x + 3', color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Equation')
plt.grid(True)
plt.legend()

# Plot the quadratic equation
plt.subplot(1, 2, 2)
plt.plot(x, y_quadratic, label='y = x^2 - 2x + 1', color='black')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quadratic Equation')
plt.grid(True)
plt.legend()

# Plot the quadratic equation
plt.subplot(1, 2, 2)
plt.plot(x, y_quadratic_inv, label='y = x^2 - 2x + 1', color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quadratic Equation+INV')
plt.grid(True)
plt.legend()

# Adjust layout for subplots
plt.tight_layout()

# Display the graph
plt.show()
