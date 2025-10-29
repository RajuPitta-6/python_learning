import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Ravi', 'Anu', 'Sita', 'Raju'],
    'Department': ['IT', 'HR', 'Finance', 'IT'],
    'Salary': [60000, 52000, 58000, 65000]
})

# Map values in Department
df['Department_Code'] = df['Department'].map({'IT': 101, 'HR': 102, 'Finance': 103})
print(df)
#    Name Department  Salary  Department_Code
# 0  Ravi         IT   60000              101
# 1   Anu         HR   52000              102
# 2  Sita    Finance   58000              103
# 3  Raju         IT   65000              101
# Functional example
df['Tax'] = df['Salary'].map(lambda x: x * 0.1)
print(df)
#    Name Department  Salary  Department_Code     Tax
# 0  Ravi         IT   60000              101  6000.0
# 1   Anu         HR   52000              102  5200.0
# 2  Sita    Finance   58000              103  5800.0
# 3  Raju         IT   65000              101  6500.0

# apply() – Works on DataFrame or Series
df['Net_Salary'] = df['Salary'].apply(lambda x: x - (x * 0.1))
print(df)
#    Name Department  Salary  Department_Code     Tax  Net_Salary
# 0  Ravi         IT   60000              101  6000.0     54000.0
# 1   Anu         HR   52000              102  5200.0     46800.0
# 2  Sita    Finance   58000              103  5800.0     52200.0
# 3  Raju         IT   65000              101  6500.0     58500.0


# applymap() – Works element-wise on whole DataFrame
df_str = df[['Name', 'Department']]

# Convert everything to uppercase
df_str = df_str.applymap(lambda x: x.upper())
print(df_str)
#    Name Department
# 0  RAVI         IT
# 1   ANU         HR
# 2  SITA    FINANCE
# 3  RAJU         IT

# Using Custom Python Functions
def salary_grade(sal):
    if sal >= 60000:
        return 'High'
    elif sal >= 55000:
        return 'Medium'
    else:
        return 'Low'

df['Grade'] = df['Salary'].apply(salary_grade)
print(df)
#   Name Department  Salary  Department_Code     Tax  Net_Salary   Grade
# 0  Ravi         IT   60000              101  6000.0     54000.0    High
# 1   Anu         HR   52000              102  5200.0     46800.0     Low
# 2  Sita    Finance   58000              103  5800.0     52200.0  Medium
# 3  Raju         IT   65000              101  6500.0     58500.0    High
df['Bonus'] = np.where(df['Department'] == 'IT', 5000, 2000)
print(df)

#   Name Department  Salary  Department_Code     Tax  Net_Salary   Grade  Bonus       
# 0  Ravi         IT   60000              101  6000.0     54000.0    High   5000       
# 1   Anu         HR   52000              102  5200.0     46800.0     Low   2000       
# 2  Sita    Finance   58000              103  5800.0     52200.0  Medium   2000       
# 3  Raju         IT   65000              101  6500.0     58500.0    High   5000 