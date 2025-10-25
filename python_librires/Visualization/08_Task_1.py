import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, color='red', marker = 'o', markerfacecolor = 'green', linestyle = '--')
plt.title("Task 1")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("Data")
plt.show()


# Bar graph
values = [10, 29, 25, 30, 40]
names = ['A', 'B', 'C', "D", 'E']

plt.bar(names, values, color = 'black')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

import numpy as np

x = np.arange(len(['A', 'B', 'C', 'D', 'E']))
y1 = [10, 24, 36, 40, 5]
y2 = [8, 30, 20, 35, 10]
plt.bar(x - 0.2, y1, width=0.4, label='2024', color='lightblue')
plt.bar(x + 0.2, y2, width=0.4, label='2025', color='lightgreen')

plt.xticks(x, ['A', 'B', 'C', 'D', 'E'])
plt.legend()
plt.title("Yearly Sales Comparison")
plt.show()

# Scatter plot
y1 = [10, 24, 36, 40, 5]
y2 = [8, 30, 20, 35, 10]

plt.scatter(y1, y2)
plt.title("Example for scatter plot")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(linestyle = ':', linewidth = 2, color = 'black')
plt.show()

# Histogram 
plt.figure(figsize=(10, 7))
plt.subplot(1, 2, 1)
marks = [30,35,40,40,45,50,55,60,60,65,70,75,80,90]
plt.hist(marks, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Marks Range')
plt.ylabel('Count')
plt.title('Marks Distribution')

# pie chart
# Data
plt.subplot(1, 2, 2)
labels = ['Python', 'Java', 'C++', 'C', 'JavaScript']
sizes = [30, 25, 15, 10, 20]

colors = ['skyblue', 'orange', 'lightgreen', 'pink', 'violet']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',pctdistance=0.85, labeldistance=1.1, explode=[0,0.1,0,0,0],shadow = True, startangle = 90)
plt.title("Programming Language Popularity", fontsize = 16, fontweight = 'bold')
plt.axis('equal')
plt.legend(title="Languages", loc="upper left")
plt.tight_layout()
plt.savefig("customized_plot_day3.png", dpi=300, bbox_inches='tight')
plt.show()