import matplotlib.pyplot as plt

# Read data from file
with open("output_data.txt", "r") as file:
    lines = file.readlines()
    data = [line.split() for line in lines[1:]]  # Skip the header line and split each line into a list

# Extract t and y(t) values
t_values = [float(row[0]) for row in data]
y_values = [float(row[1]) for row in data]

# Plot
plt.stem(t_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')  # 'b-' is for blue line, 'bo' is for blue circles at each point, 'r-' is for red baseline
plt.title('Stem Plot of y(t) vs. t')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.savefig('plot.png')
plt.show()
