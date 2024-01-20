import numpy as np
import matplotlib.pyplot as plt

# Given values
a = 6.25
d = 6.25

# Define the step function u(n)
def u(n):
    return np.heaviside(n, 1)

# Generate values for integer n
n_values_integer = np.arange(-10, 11, 1)

# Calculate the corresponding values for (a + nd) * u(n)
result_values = (a + n_values_integer * d) * u(n_values_integer)

# Plot the graph
plt.plot(n_values_integer, result_values, marker='o')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Graph of y(n) = (a + nd) * u(n) for Integer n values')

# Set x-axis labels as integers from -10 to 10 and y-axis labels starting from 6.25
plt.xticks(np.arange(-10, 11, 1))
plt.yticks(np.arange(6.25, 11 * 6.25 + 6.25, 6.25))

plt.grid(True)
plt.show()

