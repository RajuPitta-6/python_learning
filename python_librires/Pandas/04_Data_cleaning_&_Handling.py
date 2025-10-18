import pandas as pd
import numpy as np

data = {
    'Name': ['Raju', 'Sita', 'Gita', 'Ravi', 'Anu'],
    'Age': [21,np.nan, 20, 23, np.nan],
    'Score': [85, 90, np.nan, 80, 88]
}
df = pd.DataFrame(data)
print(df)
#   Name   Age  Score
# 0  Raju  21.0   85.0
# 1  Sita   NaN   90.0
# 2  Gita  20.0    NaN
# 3  Ravi  23.0   80.0
# 4   Anu   NaN   88.0


# Check which values are missing----------------------
print(df.isnull())       # True where value is NaN
#    Name    Age  Score
# 0  False  False  False
# 1  False   True  False
# 2  False  False   True
# 3  False  False  False
# 4  False   True  False
print(df.notnull())      # Opposite of isnull()
#  Name    Age  Score
# 0  True   True   True
# 1  True  False   True
# 2  True   True  False
# 3  True   True   True
# 4  True  False   True
print(df.isnull().sum()) # Count missing values per column
# Name     0
# Age      2
# Score    1
# dtype: int64

# Handle Missing Values-----------------------------
# (a) Drop rows or columns with missing values
df_drop_row = df.dropna()             # Drop rows with NaN
df_drop_col = df.dropna(axis=1)       # Drop columns with NaN
print(df_drop_row)
#  Name   Age  Score
# 0  Raju  21.0   85.0
# 3  Ravi  23.0   80.0

# Fill missing values with a constant
df_filled = df.fillna(0)
print(df_filled)
#  Name   Age  Score
# 0  Raju  21.0   85.0
# 1  Sita   0.0   90.0
# 2  Gita  20.0    0.0
# 3  Ravi  23.0   80.0
# 4   Anu   0.0   88.0

# Fill with column mean, median, or mode---------------------
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Score'].fillna(df['Score'].median(), inplace=True)
print(df)

#    Name        Age  Score
# 0  Raju  21.000000   85.0
# 1  Sita  21.333333   90.0
# 2  Gita  20.000000   86.5
# 3  Ravi  23.000000   80.0
# 4   Anu  21.333333   88.0

df = pd.DataFrame(data)
# Forward-fill & Backward-fill
df.fillna(method='ffill', inplace=True)  # Fill using previous value
# or
print(df)
#  Name   Age  Score
# 0  Raju  21.0   85.0
# 1  Sita  21.0   90.0
# 2  Gita  20.0   90.0
# 3  Ravi  23.0   80.0
# 4   Anu  23.0   88.0

df = pd.DataFrame(data)

df.fillna(method='bfill', inplace=True)  # Fill using next value
print(df)
#  Name   Age  Score
# 0  Raju  21.0   85.0
# 1  Sita  20.0   90.0
# 2  Gita  20.0   80.0
# 3  Ravi  23.0   80.0
# 4   Anu   NaN   88.0

# Replacing Specific Values----------------------------------
df.replace(80, 85, inplace=True)    # Replace score 80 → 85
df.replace({'Raju':'Rajesh'}, inplace=True)
print(df)
#  Name   Age  Score
# 0  Rajesh  21.0   85.0
# 1    Sita  20.0   90.0
# 2    Gita  20.0   85.0
# 3    Ravi  23.0   85.0
# 4     Anu   NaN   88.0

# Renaming Columns--------------------
df.rename(columns={'Score':'Marks'}, inplace=True)
print(df.head())
#    Name   Age  Marks
# 0  Rajesh  21.0   85.0
# 1    Sita  20.0   90.0
# 2    Gita  20.0   85.0
# 3    Ravi  23.0   85.0
# 4     Anu   NaN   88.0