import pandas as pd

# Concatenation (pd.concat)
# Combine vertically (stack DataFrames)
df1 = pd.DataFrame({'Name': ['A', 'B', 'C'], 'Marks': [80, 85, 90]})
df2 = pd.DataFrame({'Name': ['A', 'E', 'F'], 'Marks': [75, 88, 92]})

combined = pd.concat([df1, df2])
print(combined)
#   Name  Marks
# 0    A     80
# 1    B     85
# 2    C     90
# 0    A     75
# 1    E     88
# 2    F     92

# Combine horizontally (side by side)
combined_side = pd.concat([df1, df2], axis=1)
print(combined_side)
#   Name  Marks Name  Marks
# 0    A     80    A     75
# 1    B     85    E     88
# 2    C     90    F     92

# Reset index after concatenation
combined = pd.concat([df1, df2], ignore_index=True)
print(combined)
#  Name  Marks
# 0    A     80
# 1    B     85
# 2    C     90
# 3    A     75
# 4    E     88
# 5    F     92

# Employee information
emp = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104],
    'Name': ['Ravi', 'Sita', 'Anu', 'Raju'],
    'Department': ['HR', 'IT', 'Finance', 'IT']
})

# Salary details
sal = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 105],
    'Salary': [50000, 60000, 55000, 52000]
})

print("Employee Table:\n", emp)
print("\nSalary Table:\n", sal)

# Merge (pd.merge)
# Inner Join → Keeps matching rows only
inner_merge = pd.merge(emp, sal, on='Emp_ID', how='inner')
print(inner_merge)

# Left Join → Keeps all from left DataFrame
left_merge = pd.merge(emp, sal, on='Emp_ID', how='left')
print(left_merge)
#   Emp_ID  Name Department   Salary
# 0     101  Ravi         HR  50000.0
# 1     102  Sita         IT  60000.0
# 2     103   Anu    Finance  55000.0
# 3     104  Raju         IT      NaN

# Right Join → Keeps all from right DataFrame
right_merge = pd.merge(emp, sal, on='Emp_ID', how='right')
print(right_merge)
#    Emp_ID  Name Department  Salary
# 0     101  Ravi         HR   50000
# 1     102  Sita         IT   60000
# 2     103   Anu    Finance   55000
# 3     105   NaN        NaN   52000

# Outer Join → Keeps all rows from both
outer_merge = pd.merge(emp, sal, on='Emp_ID', how='outer')
print(outer_merge)
#   Emp_ID  Name Department   Salary
# 0     101  Ravi         HR  50000.0
# 1     102  Sita         IT  60000.0
# 2     103   Anu    Finance  55000.0
# 3     104  Raju         IT      NaN
# 4     105   NaN        NaN  52000.0

# Merge on Different Column Names
dept = pd.DataFrame({
    'Dept': ['HR', 'IT', 'Finance'],
    'Manager': ['Kiran', 'Varun', 'Anita']
})

merged = pd.merge(emp, dept, left_on='Department', right_on='Dept', how='left')
print(merged)
#   Emp_ID  Name Department     Dept Manager
# 0     101  Ravi         HR       HR   Kiran
# 1     102  Sita         IT       IT   Varun
# 2     103   Anu    Finance  Finance   Anita
# 3     104  Raju         IT       IT   Varun

# Joining using Index
df_left = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])
df_right = pd.DataFrame({'B': [4, 5, 6]}, index=['x', 'y', 'a'])

joined = df_left.join(df_right, how='outer')
print(joined)
#     A    B
# a  NaN  6.0
# x  1.0  4.0
# y  2.0  5.0
# z  3.0  NaN

# Adding Identifiers in Concatenation
df1 = pd.DataFrame({'City': ['Hyderabad', 'Delhi'], 'Population': [40, 30]})
df2 = pd.DataFrame({'City': ['Mumbai', 'Pune'], 'Population': [50, 20]})

combined = pd.concat([df1, df2], keys=['State1', 'State2'])
print(combined)

# Handling Duplicates After Merge
emp_details = pd.merge(emp, sal, on='Emp_ID', how='outer', suffixes=('_Emp', '_Sal'))
print(emp_details)
