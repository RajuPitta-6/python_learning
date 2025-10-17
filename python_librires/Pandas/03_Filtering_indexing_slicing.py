import pandas as pd

data = {
    'Name': ['Raju', 'Sita', 'Gita', 'Ravi', 'Anu'],
    'Age': [21, 22, 20, 23, 19],
    'Score': [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)
print(df)
#   Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95
# 3  Ravi   23     80
# 4   Anu   19     88

# Filter by one condition---------------------
print(df[df['Score'] > 85])  # Students who scored more than 85
#    Name  Age  Score
# 1  Sita   22     90
# 2  Gita   20     95
# 4   Anu   19     88

# Filter by multiple conditions--------------------
# Students who scored >85 AND age <22
print(df[(df['Score'] > 85) & (df['Age'] < 22)])
#   Name  Age  Score
# 2  Gita   20     95
# 4   Anu   19     88
# Students who scored >90 OR age <21
print(df[(df['Score'] > 90) | (df['Age'] < 21)])
#   Name  Age  Score
# 2  Gita   20     95
# 4   Anu   19     88

# Filter by string match--------------
print(df[df['Name'].str.startswith('R')])  # Names starting with 'R'
#    Name  Age  Score
# 0  Raju   21     85
# 3  Ravi   23     80

# 2. loc[] for Label-based Indexing
# Syntax: df.loc[row_labels, column_labels]
print(df.loc[0])                 # Row with label 0
# Name     Raju
# Age        21
# Score      85
# Name: 0, dtype: object
print(df.loc[0:2, ['Name','Score']])  # Rows 0 to 2, specific columns
#  Name  Score
# 0  Raju     85
# 1  Sita     90
# 2  Gita     95
print(df.loc[df['Score']>85, ['Name','Score']])  # Filtered view
#  Name  Score
# 1  Sita     90
# 2  Gita     95
# 4   Anu     88

# 3.iloc[] for Position-based Indexing
# Syntax: df.iloc[row_index, column_index]
print(df.iloc[0])           # First row
# Name     Raju
# Age        21
# Score      85
# Name: 0, dtype: object
print(df.iloc[0:3, 0:2])    # Rows 0–2 and columns 0–1
#   Name  Age
# 0  Raju   21
# 1  Sita   22
# 2  Gita   20
print(df.iloc[[0,2,4], [0,2]])  # Specific rows & columns
#   Name  Score
# 0  Raju     85
# 2  Gita     95
# 4   Anu     88

# 4. Slicing Rows and Columns-----------------------
print(df[1:4])               # Rows 1 to 3
#  Name  Age  Score
# 1  Sita   22     90
# 2  Gita   20     95
# 3  Ravi   23     80

print(df.loc[:, 'Name':'Score'])  # All rows, Name → Score columns
#    Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95
# 3  Ravi   23     80
# 4   Anu   19     88
print(df.iloc[:, 1:])        # All rows, columns 1 onwards
#   Age  Score
# 0   21     85
# 1   22     90
# 2   20     95
# 3   23     80
# 4   19     88

# 5. Conditional Assignment----------------------------
df.loc[df['Score'] < 85, 'Score'] = 85
print(df)
#  Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95
# 3  Ravi   23     85
# 4   Anu   19     88

# 6. Using isin() to Filter Multiple Values-------------------
print(df[df['Name'].isin(['Raju', 'Anu'])])
#    Name  Age  Score
# 0  Raju   21     85
# 4   Anu   19     88

# 7. Using between() for Range Filtering----------------
print(df[df['Age'].between(20, 22)])
#    Name  Age  Score
# 0  Raju   21     85
# 1  Sita   22     90
# 2  Gita   20     95

# 8.Using query() for SQL-like Filtering
print(df.query('Score > 85 and Age < 22'))
#   Name  Age  Score
# 2  Gita   20     95
# 4   Anu   19     88