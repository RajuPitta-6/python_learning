import matplotlib.pyplot as plt

# plot the population growth for 5 years 2020-2025
x = [2020, 2021, 2022, 2023, 2024]
y = [78698, 78292, 79391, 80192, 80932]

plt.plot(x, y)
plt.title("Population growth rate for 5 years")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()


# 2.Create chart for marks of 4 subjects------------
subject = ['Math', 'Computer', 'Chemistry', 'Physics']
marks = [99, 95, 65, 80]

plt.bar(subject, marks, color = 'green')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()

# 3.Make a scatter plot of height vs weight for 5 students
height = [183, 250, 200, 220, 180]
weight = [70, 99, 80, 93, 68]

plt.scatter(weight, height, color='red')
plt.title("Height vs Weight")
plt.ylabel("Height")
plt.xlabel("Weight")
plt.show()