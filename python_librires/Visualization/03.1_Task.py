'''
🧠 Mini Practice Tasks

Try these to master customization 👇

1️⃣ Plot a dashed red line with circular markers and a title.
2️⃣ Add gridlines and an annotation showing the highest point in a dataset.
3️⃣ Create a styled plot using 'ggplot' style and save it as "styled_output.png".
4️⃣ Change figure size to 10x6 and experiment with fontsize, fontweight.
'''

import matplotlib.pyplot as plt


# 1️⃣ Plot a dashed red line with circular markers and a title.

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, color = 'black', linestyle = '--', linewidth = 3, marker = 'o', markersize = 8, markerfacecolor = 'orange')
plt.title("customized plot")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

#  Add gridlines and an annotation showing the highest point in a dataset.
# Create a styled plot using 'ggplot' style and save it as "styled_output.png".
#  Change figure size to 10x6 and experiment with fontsize, fontweight.

# Use ggplot style
plt.style.use('ggplot')

# Sample dataset
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Create figure with size 10x6
plt.figure(figsize=(10, 5))

# Plot the data
plt.plot(x, y, marker='o', label='Data')

# Add gridlines
plt.grid(True)

# Annotate the highest point
max_x = x[y.index(max(y))]
max_y = max(y)
plt.annotate('Highest Point',
             xy=(max_x, max_y),
             xytext=(max_x-2, max_y+5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12,
             fontweight='bold')

# Customize labels and title
plt.xlabel('X-axis', fontsize=14, fontweight='bold')
plt.ylabel('Y-axis', fontsize=14, fontweight='bold')
plt.title('Styled Plot with Annotation', fontsize=16, fontweight='bold')
plt.legend()

# Save the figure
plt.savefig('styled_output.png')

# Show the plot
plt.show()
