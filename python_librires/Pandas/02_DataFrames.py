import pandas as pd

# creating DataFarmes From a dictionary-------------------
import pandas as pd

data = {
    'Name': ['Raju', 'Sita', 'Gita'],
    'Age': [21, 22, 20],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)
print(df)
#    Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95

# Creating DataFrame From a list of lists
data = [
    ['Raju', 21, 85],
    ['Sita', 22, 90],
    ['Gita', 20, 95]
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])
print(df)
#    Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95

# Creating DataFrame From a list of dictionaries
data = [
    {'Name':'Raju','Age':21,'Score':85},
    {'Name':'Sita','Age':22,'Score':90},
    {'Name':'Gita','Age':20,'Score':95}
]
df = pd.DataFrame(data)
print(df)
#    Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95

# Viewing Data-----------------------
print(df.head()) # By default gives first 5 rows
#    Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95

print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    3 non-null      object
#  1   Age     3 non-null      int64
#  2   Score   3 non-null      int64
# dtypes: int64(2), object(1)
# memory usage: 204.0+ bytes
# None
print(df.describe())
#         Age  Score
# count   3.0    3.0
# mean   21.0   90.0
# std     1.0    5.0
# min    20.0   85.0
# 25%    20.5   87.5
# 50%    21.0   90.0
# 75%    21.5   92.5
# max    22.0   95.0

# Accessing Columns & Rows------------------

# coloumns
print(df['Name'])  # Single column → Series
# 0    Raju
# 1    Sita
# 2    Gita
print(df[['Name', 'Age']])  # Multiple columns → DataFrame
#   Name  Age
# 0  Raju   21
# 1  Sita   22
# 2  Gita   20

# Rows
print(df.loc[1])   # Row by label/index
# Name     Sita
# Age        22
# Score      90
# Name: 1, dtype: object
print(df.iloc[1])  # Row by position
# Name     Sita
# Age        22
# Score      90
# Name: 1, dtype: object

# Rows & Columns
print(df.loc[0, 'Name'])   # Specific cell
# Raju
print(df.iloc[0, 1])       # Same using position
# 21

# Adding / Modifying Columns--------------------
df['Passed'] = [True, True, True]  # Add new column
df['Score'] = df['Score'] + 5      # Modify column
print(df)
#    Name  Age  Score  Passed
# 0  Raju   21     90    True
# 1  Sita   22     95    True
# 2  Gita   20    100    True

# Deleting Columns--------------------
df.drop('Passed', axis=1, inplace=True)  # Drop column permanently
print(df)
#  Name  Age  Score
# 0  Raju   21     90
# 1  Sita   22     95
# 2  Gita   20    100

# Basic Operations------------------
print(df['Score'].sum())     # Sum of scores
print(df['Score'].mean())    # Average score
print(df['Score'].max())     # Maximum score
# 285
# 95.0
# 100