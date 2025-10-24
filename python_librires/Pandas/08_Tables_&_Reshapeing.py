# Syntax :
# DataFrame.pivot_table(values, index, columns, aggfunc)
import pandas as pd

# Sample data
data = {
    'Department': ['IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Gender': ['M', 'F', 'M', 'F', 'F', 'M', 'M'],
    'Salary': [70000, 48000, 60000, 52000, 50000, 62000, 72000]
}

df = pd.DataFrame(data)
print(df)

# Create Pivot Table
# Average salary by Department and Gender
pivot = df.pivot_table(values='Salary', index='Department', columns='Gender', aggfunc='mean')
print(pivot)
# Gender            F        M
# Department
# Finance         NaN  61000.0
# HR          49000.0      NaN
# IT          52000.0  71000.0

# Multiple Aggregations
m = df.pivot_table(values='Salary', index='Department', aggfunc=['mean', 'max', 'min'])
print(m)
                    # mean    max    min
#                   Salary Salary Salary
# Department
# Finance     61000.000000  62000  60000
# HR          49000.000000  50000  48000
# IT          64666.666667  72000  52000

# Crosstab (Frequency Table)
c = pd.crosstab(df['Department'], df['Gender'])
print(c)
# Gender      F  M
# Department
# Finance     0  2
# HR          2  0
# IT          1  2

# Reshaping Data – melt(), stack(), unstack()

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob'],
    'Math': [90, 80],
    'Science': [85, 75]
}
df = pd.DataFrame(data)

print(df)

# Use melt()
melted = pd.melt(df, id_vars=['Name'], var_name='Subject', value_name='Marks')
print(melted)
#     Name  Subject  Marks
# 0  Alice     Math     90
# 1    Bob     Math     80
# 2  Alice  Science     85
# 3    Bob  Science     75

#  stack() & unstack()
df2 = df.set_index('Name')
stacked = df2.stack()
print(stacked)
# Name
# Alice  Math       90
#        Science    85
# Bob    Math       80
#        Science    75
# dtype: int64

unstacked = stacked.unstack()
print(unstacked)
#       Math  Science
# Name
# Alice    90       85
# Bob      80       75