import pandas as pd

data = {
    'Name': ['Ravi', 'Anu', 'Sita', 'Raju', 'Gita', 'Balu'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Salary': [60000, 52000, 58000, 65000, 57000, 49000],
    'Experience': [3, 2, 5, 4, 7, 1]
}

df = pd.DataFrame(data)
print(df)

# Sorting Data------------------------

# a) Sort by a single column (ascending)
print(df.sort_values('Salary'))
#   Name Department  Salary  Experience
# 5  Balu         HR   49000           1
# 1   Anu         HR   52000           2
# 4  Gita    Finance   57000           7
# 2  Sita    Finance   58000           5
# 0  Ravi         IT   60000           3
# 3  Raju         IT   65000           4

# b) Sort by a single column (descending)
print(df.sort_values('Salary', ascending=False))
#    Name Department  Salary  Experience
# 3  Raju         IT   65000           4
# 0  Ravi         IT   60000           3
# 2  Sita    Finance   58000           5
# 4  Gita    Finance   57000           7
# 1   Anu         HR   52000           2
# 5  Balu         HR   49000           1

# c) Sort by multiple columns
print(df.sort_values(['Department', 'Salary'], ascending=[True, False]))
#   Name Department  Salary  Experience
# 2  Sita    Finance   58000           5
# 4  Gita    Finance   57000           7
# 1   Anu         HR   52000           2
# 5  Balu         HR   49000           1
# 3  Raju         IT   65000           4
# 0  Ravi         IT   60000           3



# Sorting by Index----------------
# Sort rows by index labels
df_sorted_index = df.sort_index()
print(df_sorted_index)

# Sort columns alphabetically-
df_sorted_cols = df.sort_index(axis=1)
print(df_sorted_cols)
#   Department  Experience  Name  Salary
# 0         IT           3  Ravi   60000
# 1         HR           2   Anu   52000
# 2    Finance           5  Sita   58000
# 3         IT           4  Raju   65000
# 4    Finance           7  Gita   57000
# 5         HR           1  Balu   49000

# Ranking Data----
# Rank salary values
df['Salary_Rank'] = df['Salary'].rank()
print(df)
#    Name Department  Salary  Experience  Salary_Rank
# 0  Ravi         IT   60000           3          5.0
# 1   Anu         HR   52000           2          2.0
# 2  Sita    Finance   58000           5          4.0
# 3  Raju         IT   65000           4          6.0
# 4  Gita    Finance   57000           7          3.0
# 5  Balu         HR   49000           1          1.0

# Rank in descending order
df['Salary_Rank_Desc'] = df['Salary'].rank(ascending=False)
print(df)

# Ranking method variations------------
df['Dense_Rank'] = df['Salary'].rank(method='dense', ascending=False)
df['Min_Rank'] = df['Salary'].rank(method='min', ascending=False)
df['Max_Rank'] = df['Salary'].rank(method='max', ascending=False)
print(df)

#    Name Department  Salary  ...  Dense_Rank  Min_Rank  Max_Rank
# 0  Ravi         IT   60000  ...         2.0       2.0       2.0
# 1   Anu         HR   52000  ...         5.0       5.0       5.0
# 2  Sita    Finance   58000  ...         3.0       3.0       3.0
# 3  Raju         IT   65000  ...         1.0       1.0       1.0
# 4  Gita    Finance   57000  ...         4.0       4.0       4.0
# 5  Balu         HR   49000  ...         6.0       6.0       6.0

# [6 rows x 9 columns]


# Index Operations-----------

# Set a column as index---------------
df2 = df.set_index('Name')
print(df2)
#    Department  Salary  Experience  ...  Dense_Rank  Min_Rank  Max_Rank
# Name                                 ...
# Ravi         IT   60000           3  ...         2.0       2.0       2.0
# Anu          HR   52000           2  ...         5.0       5.0       5.0
# Sita    Finance   58000           5  ...         3.0       3.0       3.0
# Raju         IT   65000           4  ...         1.0       1.0       1.0
# Gita    Finance   57000           7  ...         4.0       4.0       4.0
# Balu         HR   49000           1  ...         6.0       6.0       6.0

# [6 rows x 8 columns]

# Reset index-----------
df2.reset_index(inplace=True)
print(df2)
#    Name Department  Salary  ...  Dense_Rank  Min_Rank  Max_Rank
# 0  Ravi         IT   60000  ...         2.0       2.0       2.0
# 1   Anu         HR   52000  ...         5.0       5.0       5.0
# 2  Sita    Finance   58000  ...         3.0       3.0       3.0
# 3  Raju         IT   65000  ...         1.0       1.0       1.0
# 4  Gita    Finance   57000  ...         4.0       4.0       4.0
# 5  Balu         HR   49000  ...         6.0       6.0       6.0

# [6 rows x 9 columns]

# Rename index------
df2.index.name = 'Row_ID'
print(df2)
#         Name Department  Salary  ...  Dense_Rank  Min_Rank  Max_Rank
# Row_ID                           ...
# 0       Ravi         IT   60000  ...         2.0       2.0       2.0
# 1        Anu         HR   52000  ...         5.0       5.0       5.0
# 2       Sita    Finance   58000  ...         3.0       3.0       3.0
# 3       Raju         IT   65000  ...         1.0       1.0       1.0
# 4       Gita    Finance   57000  ...         4.0       4.0       4.0
# 5       Balu         HR   49000  ...         6.0       6.0       6.0

# [6 rows x 9 columns]

# Reindexing-------------
new_index = [2, 0, 5, 1, 4, 3]
df_reindexed = df.reindex(new_index)
print(df_reindexed)
#   Name Department  Salary  ...  Dense_Rank  Min_Rank  Max_Rank
# 2  Sita    Finance   58000  ...         3.0       3.0       3.0
# 0  Ravi         IT   60000  ...         2.0       2.0       2.0
# 5  Balu         HR   49000  ...         6.0       6.0       6.0
# 1   Anu         HR   52000  ...         5.0       5.0       5.0
# 4  Gita    Finance   57000  ...         4.0       4.0       4.0
# 3  Raju         IT   65000  ...         1.0       1.0       1.0

# [6 rows x 9 columns]

df_reordered = df.reindex(columns=['Department', 'Name', 'Salary', 'Experience'])
print(df_reordered)
#  Department  Name  Salary  Experience
# 0         IT  Ravi   60000           3
# 1         HR   Anu   52000           2
# 2    Finance  Sita   58000           5
# 3         IT  Raju   65000           4
# 4    Finance  Gita   57000           7
# 5         HR  Balu   49000           1

# Detecting and Handling Missing Indexes
# df_new = df.reindex([0, 1, 2, 10])  # 10 doesn’t exist
# print(df_new.fillna('Missing'))
