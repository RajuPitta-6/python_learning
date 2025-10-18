import matplotlib.pyplot as plt
import numpy as np

# Histogram (Data distribution)
data = np.random.randn(1000) 
plt.hist(data, bins=20, color = 'skyblue')
plt.title("Histogram Example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# Pie chart
labels = ["Python", 'C', "Java", 'C++']
sizes = [45, 25, 20, 10]
col = ['gold', 'skyblue', 'lightgreen', 'pink']
plt.pie(sizes, labels=labels, colors=col, autopct="%1.1f%%", startangle=90)
plt.title("Programing language popularity")
plt.show()

# Box plot
maths = np.random.randint(40, 100, 25)
science = np.random.randint(40, 100, 25)
english = np.random.randint(40, 100, 25)
plt.boxplot([maths, science, english], labels = ['Maths', 'Science', 'English'])
plt.title("Boxplot of marks Distribution")
plt.ylabel("Marks")
plt.show()

# subplots
x = np.arange(1, 6)
y1 = x**2
y2 = x**3

# create sublots (1 row 2 coloumns)
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1, color = 'blue')
plt.title("Squre Function")

plt.subplot(1, 2, 2)
plt.plot(x, y2, color = 'red')
plt.title("Cube Function")

plt.tight_layout()
plt.show()