import pandas as pd

data = {
    'Name': ['Ravi', 'Anu', 'Sita', 'Raju', 'Gita', 'Balu'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Salary': [60000, 52000, 58000, 65000, 57000, 49000],
    'Experience': [3, 2, 5, 4, 7, 1]
}

df = pd.DataFrame(data)
print(df)

#  Sort by a single column (ascending)
print(df.sort_values('Salary'))