# ✅ Day 6 Practice Tasks

# Create your own DataFrame with at least 6 rows.

# Sort data by one column (ascending/descending).

# Sort data by two columns (e.g., Department → Salary).

# Rank employees by their Salary (ascending and descending).

# Set “Name” as index and reset it again.

# Reindex your DataFrame in a custom order.

# Try renaming the index and reordering columns.
import pandas as pd

data = {
    'Name': ['Ravi', 'Anu', 'Sita', 'Raju', 'Gita', 'Balu'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Salary': [60000, 52000, 58000, 65000, 57000, 49000],
    'Experience': [3, 2, 5, 4, 7, 1]
}

df = pd.DataFrame(data)

# Sort data by one column (ascending/descending).
print(df.sort_values('Salary', ascending=False))
#    Name Department  Salary  Experience
# 3  Raju         IT   65000           4
# 0  Ravi         IT   60000           3
# 2  Sita    Finance   58000           5
# 4  Gita    Finance   57000           7
# 1   Anu         HR   52000           2
# 5  Balu         HR   49000           1

# Sort data by two columns (e.g., Department → Salary).
print(df.sort_values(['Salary', 'Department'], ascending=[False, True]))
#    Name Department  Salary  Experience
# 3  Raju         IT   65000           4
# 0  Ravi         IT   60000           3
# 2  Sita    Finance   58000           5
# 4  Gita    Finance   57000           7
# 1   Anu         HR   52000           2
# 5  Balu         HR   49000           1

# Rank employees by their Salary (ascending and descending).

df['Salary_Rank'] = df['Salary'].rank(ascending= False)
print(df)
#  Name Department  Salary  Experience  Salary_Rank
# 0  Ravi         IT   60000           3          2.0
# 1   Anu         HR   52000           2          5.0
# 2  Sita    Finance   58000           5          3.0
# 3  Raju         IT   65000           4          1.0
# 4  Gita    Finance   57000           7          4.0
# 5  Balu         HR   49000           1          6.0

# Set “Name” as index and reset it again.
# df.set_index("Name", inplace= True)
# print(df)

df.sort_values(by='Salary_Rank', ascending=True, inplace=True)
df['S.No'] = range(1, len(df)+1)
col = df.pop('S.No')
df.insert(0, 'S.No',col)
print(df.to_string(index=False))

#  S.No Name Department  Salary  Experience  Salary_Rank
#     1 Raju         IT   65000           4          1.0
#     2 Ravi         IT   60000           3          2.0
#     3 Sita    Finance   58000           5          3.0
#     4 Gita    Finance   57000           7          4.0
#     5  Anu         HR   52000           2          5.0
#     6 Balu         HR   49000           1          6.0