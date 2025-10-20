'''
✅ Module 5 Practice Tasks

Create a DataFrame with columns: Department, Employee, Salary, Experience

Find:

Average salary per department

Total salary per department

Highest experience per department

Use .agg() for multiple metrics like mean, min, max

Group by both Department and Experience

Filter departments whose average salary > 55,000

Use .transform() to add a Mean_Salary column

Sort results by average salary (descending)

Try a custom function in .apply()'''

import pandas as pd

# Create a DataFrame with columns: Department, Employee, Salary, Experience
data = {
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Salary': [50000, 60000, 65000, 55000, 52000, 58000, 70000, 49000],
    'Experience': [2, 3, 5, 4, 1, 6, 7, 2]
}

df = pd.DataFrame(data)
print(df)

# Average salary per department
avg_salary = df.groupby('Department')['Salary'] .mean()
print(avg_salary)

# Total salary per department
High_salary = df.groupby('Department')['Salary'] .max()
print(High_salary)

# Total salary per department
Total_salary = df.groupby('Department')['Salary'] .sum()
print(Total_salary)

# Highest experience per department
High_exp = df.groupby('Department')['Experience'] .max()
print(High_exp)

# Use .agg() for multiple metrics like mean, min, max
detail = df.groupby('Department').agg({
    'Salary' : ['max', 'min', 'sum', 'mean'],
    'Experience' : ['max', 'min', 'mean']
})

print(detail)

# Group by both Department and Experience

G = df.groupby(['Department', 'Experience'])['Salary'].max()


# Filter departments whose average salary > 55,000
filt = df[df['Salary'] > 55000]


# Sort results by average salary (descending)
result = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)


def increase(x):
  x['Salary'] +=  x['Experience'] * (x['Salary'] / 10)
  return x
result = df.groupby('Department').apply(increase)