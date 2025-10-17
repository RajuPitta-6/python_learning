import matplotlib.pyplot as plt

# Line Plot-----------------------------------
# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Basic line plot
plt.plot(x, y) # → draws a line graph.
plt.title("Simple Line Plot") # add title
plt.xlabel("X Axis") # add labels for x
plt.ylabel("y Axis") # add label for y
plt.show()

# Bar Chart--------------------------------
# Data
names = ['A', 'B', 'C', 'D']
values = [5, 8, 3, 7]

# Basic bar chart
plt.bar(names, values, color='black')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Data
names = ['A', 'B', 'C', 'D']
values = [5, 8, 3, 7]

# Scatter Plot--------------------
# Data
x = [1, 2, 3, 4, 5, 6]
y = [5, 7, 4, 6, 8, 9]

# Scatter plot
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Multiple Plots in One Figure---------------------------
# Two lines on same plot
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label='Squares', color='blue')
plt.plot(x, y2, label='Line', color='green')
plt.title("Multiple Lines Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()     # shows label box
plt.show()


# Save Your Plot----------------------------
plt.plot(x, y1, color='purple')
plt.title("Saved Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("line_plot_day1.png")  # saves in same folder
plt.show()
