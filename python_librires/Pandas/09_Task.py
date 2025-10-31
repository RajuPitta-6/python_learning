'''1️⃣ Filter rows where Email contains 'gmail'.
2️⃣ Replace all @gmail.com with @outlook.com.
3️⃣ Extract only username from email .
4️⃣ Extract domain from email using .
5️⃣ Create new column combining first and last names → FullName.'''

import pandas as pd
import numpy as np

data = {
    'Name': ['  alice ', 'BOB', '  Charlie  ', 'David', 'Eve '],
    'Email': ['alice@gmail.com', 'bob@yahoo.com', None, 'david@outlook.com', 'eve@gmail.com'],
    'City': ['delhi', 'mumbai', 'BANGALORE', np.nan, 'KOLKATA']
}

df = pd.DataFrame(data)

df['Has_gmail'] = df['Email'].str.contains('gmail', na = False)
print(df)
#           Name              Email       City  Has_gmail
# 0       alice     alice@gmail.com      delhi       True
# 1          BOB      bob@yahoo.com     mumbai      False
# 2    Charlie                 None  BANGALORE      False
# 3        David  david@outlook.com        NaN      False
# 4         Eve       eve@gmail.com    KOLKATA       True

df['Email'] = df['Email'].str.replace('gmail', 'outlook', regex=False)
print(df)
#           Name              Email       City  Has_gmail
# 0       alice   alice@outlook.com      delhi       True
# 1          BOB      bob@yahoo.com     mumbai      False
# 2    Charlie                 None  BANGALORE      False
# 3        David  david@outlook.com        NaN      False
# 4         Eve     eve@outlook.com    KOLKATA       True

df['Username'] = df['Email'].str.extract(r'(^[\w]+)')
print(df)
#           Name              Email       City  Has_gmail Username
# 0       alice   alice@outlook.com      delhi       True    alice
# 1          BOB      bob@yahoo.com     mumbai      False      bob
# 2    Charlie                 None  BANGALORE      False      NaN
# 3        David  david@outlook.com        NaN      False    david
# 4         Eve     eve@outlook.com    KOLKATA       True      eve

df['Domain'] = df['Email'].str.extract(r'@([\w]+)')
print(df)
#       Name              Email       City  Has_gmail Username   Domain
# 0       alice   alice@outlook.com      delhi       True    alice  outlook
# 1          BOB      bob@yahoo.com     mumbai      False      bob    yahoo
# 2    Charlie                 None  BANGALORE      False      NaN      NaN
# 3        David  david@outlook.com        NaN      False    david  outlook
# 4         Eve     eve@outlook.com    KOLKATA       True      eve  outlook


df['Name'] = df['Name'].str.strip()
df['Full_Name'] = df['Name'].str.cat(df['City'], sep=' - ')
print(df)
#       Name              Email       City  Has_gmail Username   Domain            Full_Name
# 0    alice  alice@outlook.com      delhi       True    alice  outlook        alice - delhi
# 1      BOB      bob@yahoo.com     mumbai      False      bob    yahoo         BOB - mumbai
# 2  Charlie               None  BANGALORE      False      NaN      NaN  Charlie - BANGALORE
# 3    David  david@outlook.com        NaN      False    david  outlook                  NaN
# 4      Eve    eve@outlook.com    KOLKATA       True      eve  outlook        Eve - KOLKATA