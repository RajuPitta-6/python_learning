import matplotlib.pyplot as plt
import numpy as np

# Create a histogram of student ages (random 50 ages between 15-25)
ages = np.random.randint(15, 25, 50)
plt.hist(ages, color='black')
plt.title("Ages")
plt.show()

# create a pie chart showing time spend on activities()

activites = ['social media', 'School', 'Online games', 'Sleep', 'others']
times = [3, 10, 1, 8, 2 ]
col = ['gold', 'skyblue', 'lightgreen', 'pink', 'green']

plt.pie(times, labels = activites, colors=col, autopct="%1.1f%%", startangle=90)
plt.title("Vinay usual timings")
plt.show()

# `Create a box plot comparing salaries of 3 departments
IAS = np.random.randint(56100, 250000, 5)
IPS = np.random.randint(53000, 225000, 5)
IRS = np.random.randint(49000, 200000, 5)

data = [IAS, IPS, IRS]
label = ["IAS", "IPS", 'IRS']
plt.boxplot(data, label=label)
plt.title("Salaries of 3 Departments")
plt.ylabel("SALARY")
plt.show()
# make 2 subplots one line plot and one bar chart side by side 
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
plt.bar(x, y2, color = 'red')
plt.xlabel("Number")
plt.ylabel("Cubes")
plt.title("Cube Function")

plt.tight_layout()
plt.show()