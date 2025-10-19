import pandas as pd

data = {
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Salary': [50000, 60000, 65000, 55000, 52000, 58000, 70000, 49000],
    'Experience': [2, 3, 5, 4, 1, 6, 7, 2]
}

df = pd.DataFrame(data)
print(df)

# Basic GroupBy
# a) Group by one column
group = df.groupby('Department')
print(group)
print(group.groups)
# {'Finance': [3, 5], 'HR': [0, 4, 7], 'IT': [1, 2, 6]}

# Aggregation Functions---------------

print(df.groupby('Department')['Salary'].mean())  # Average salary per department
# Department
# Finance    56500.000000
# HR         50333.333333
# IT         65000.000000
# Name: Salary, dtype: float64
print(df.groupby('Department')['Salary'].sum())   # Total salary
# Department
# Finance    113000
# HR         151000
# IT         195000
# Name: Salary, dtype: int64
print(df.groupby('Department')['Salary'].max())   # Highest salary
# Department
# Finance    58000
# HR         52000
# IT         70000
# Name: Salary, dtype: int64

# Multiple Aggregations-----------------
result = df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min'],
    'Experience': ['sum', 'mean']
})
print(result)
#                 Salary               Experience
#                     mean    max    min        sum      mean
# Department
# Finance     56500.000000  58000  55000         10  5.000000
# HR          50333.333333  52000  49000          5  1.666667
# IT          65000.000000  70000  60000         15  5.000000

# Group by Multiple Columns-----------
group2 = df.groupby(['Department', 'Experience'])['Salary'].mean()
print(group2)
# Department  Experience
# Finance     4             55000.0
#             6             58000.0
# HR          1             52000.0
#             2             49500.0
# IT          3             60000.0
#             5             65000.0
#             7             70000.0
# Name: Salary, dtype: float64

# Using as_index=False-------------------------
result = df.groupby('Department', as_index=False)['Salary'].mean()
print(result)  
# Department        Salary
# 0    Finance  56500.000000
# 1         HR  50333.333333
# 2         IT  65000.000000

# Sort Grouped Results------------------------
result = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
print(result)
# Department
# IT         65000.000000
# Finance    56500.000000
# HR         50333.333333

# Filter Groups------------
filtered = df.groupby('Department').filter(lambda x: x['Salary'].mean() > 55000)
print(filtered)
#  Department Employee  Salary  Experience
# 1         IT        B   60000           3
# 2         IT        C   65000           5
# 3    Finance        D   55000           4
# 5    Finance        F   58000           6
# 6         IT        G   70000           7

# Apply Custom Functions------------------
def bonus(x):
    return x['Salary'].mean() + 2000

print(df.groupby('Department').apply(bonus))
# Department
# Finance    58500.000000
# HR         52333.333333
# IT         67000.000000
# dtype: float64

# Group-wise Transformation-------------
df['Mean_Salary'] = df.groupby('Department')['Salary'].transform('mean')
print(df)
#  Department Employee  Salary  Experience   Mean_Salary
# 0         HR        A   50000           2  50333.333333
# 1         IT        B   60000           3  65000.000000
# 2         IT        C   65000           5  65000.000000
# 3    Finance        D   55000           4  56500.000000
# 4         HR        E   52000           1  50333.333333
# 5    Finance        F   58000           6  56500.000000
# 6         IT        G   70000           7  65000.000000
# 7         HR        H   49000           2  50333.333333

# Named Aggregations (Cleaner syntax)-----------

result = df.groupby('Department', as_index=False).agg(
    Avg_Salary=('Salary', 'mean'),
    Max_Exp=('Experience', 'max')
)
print(result)
#   Department    Avg_Salary  Max_Exp
# 0    Finance  56500.000000        6
# 1         HR  50333.333333        2
# 2         IT  65000.000000        7