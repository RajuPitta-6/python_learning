
'''
✅ Day 4 Practice Tasks

Create a DataFrame with some missing values

Check missing values using isnull() & sum()

Fill missing Age with mean and Score with median

Replace a specific value (e.g., 80 → 85)

Remove duplicate rows

Convert Age column from float → int

Rename Score → Marks

Strip spaces in the Name column

Reset index after cleaning'''


import pandas as pd
import numpy as np

data = {
    'Name': ['Raju', 'Sita', 'Gita', 'Ravi', 'Anu', 'swathi'],
    'Age': [21,np.nan, 20, 23, np.nan, 19],
    'Score': [85, 90, np.nan, 80, 88, 99]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())

# Fill missing Age with mean and Score with median
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Score'].fillna(df['Score'].median(), inplace=True)

# Replace a specific value (e.g., 80 → 85)
df.replace(80, 85, inplace=True)
print(df)

# Remove duplicate rows
print(df.duplicated())
df.drop_duplicates(inplace=True)

# Convert Age column from float → int
df['Age'] = df['Age'].astype(int)


# Rename Score → Marks
df.rename(columns={'Score' : 'Marks'}, inplace=True)

# Strip spaces in the Name column
df['Name'] = df['Name'].str.strip()

# Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# Finall Dataframe after clean and handle missing value
print(df)
# Before :
'''
   Name   Age  Score
0    Raju  21.0   85.0
1    Sita   NaN   90.0
2    Gita  20.0    NaN
3    Ravi  23.0   80.0
4     Anu   NaN   88.0
5  swathi  19.0   99.0'''

# After
'''  Name  Age  Marks
0    Raju   21   85.0
1    Sita   20   90.0
2    Gita   20   88.0
3    Ravi   23   85.0
4     Anu   20   88.0
5  swathi   19   99.0'''