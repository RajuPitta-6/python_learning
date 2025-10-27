import pandas as pd
import numpy as np

data = {
    'Name': ['  alice ', 'BOB', '  Charlie  ', 'David', 'Eve '],
    'Email': ['alice@gmail.com', 'bob@yahoo.com', None, 'david@outlook.com', 'eve@gmail.com'],
    'City': ['delhi', 'mumbai', 'BANGALORE', np.nan, 'KOLKATA']
}

df = pd.DataFrame(data)
print(df)
#           Name              Email       City
# 0       alice     alice@gmail.com      delhi
# 1          BOB      bob@yahoo.com     mumbai
# 2    Charlie                 None  BANGALORE
# 3        David  david@outlook.com        NaN
# 4         Eve       eve@gmail.com    KOLKATA

# Clean Spaces and Text Formatting
# Remove leading/trailing spaces
df['Name'] = df['Name'].str.strip()

# Convert case
df['Name_Lower'] = df['Name'].str.lower()
df['Name_Upper'] = df['Name'].str.upper()
df['Name_Title'] = df['Name'].str.title()

print(df[['Name', 'Name_Lower', 'Name_Upper', 'Name_Title']])
#    Name Name_Lower Name_Upper Name_Title
# 0    alice      alice      ALICE      Alice
# 1      BOB        bob        BOB        Bob
# 2  Charlie    charlie    CHARLIE    Charlie
# 3    David      david      DAVID      David
# 4      Eve        eve        EVE        Eve

# Working with City Names
df['City'] = df['City'].fillna('unknown')
df['City_Clean'] = df['City'].str.title()
print(df[['City', 'City_Clean']])
#       City City_Clean
# 0      delhi      Delhi
# 1     mumbai     Mumbai
# 2  BANGALORE  Bangalore
# 3    unknown    Unknown
# 4    KOLKATA    Kolkata

# Checking for Substrings
# Check if Email contains 'gmail'
df['Has_Gmail'] = df['Email'].str.contains('gmail', na=False)
print(df[['Email', 'Has_Gmail']])
#              Email  Has_Gmail
# 0    alice@gmail.com       True
# 1      bob@yahoo.com      False
# 2               None      False
# 3  david@outlook.com      False
# 4      eve@gmail.com       True

# Replacing Text
# Replace gmail → googlemail
df['Email'] = df['Email'].str.replace('gmail', 'googlemail', regex=True)
print(df[['Email']])
# 0  alice@googlemail.com
# 1         bob@yahoo.com
# 2                  None
# 3     david@outlook.com
# 4    eve@googlemail.com

# Extracting Parts of Strings
# Extract username and domain
df['Username'] = df['Email'].str.extract(r'(^[\w]+)')
df['Domain'] = df['Email'].str.extract(r'@([\w]+)')
print(df[['Email', 'Username', 'Domain']])
#                   Email Username      Domain
# 0  alice@googlemail.com    alice  googlemail
# 1         bob@yahoo.com      bob       yahoo
# 2                  None      NaN         NaN
# 3     david@outlook.com    david     outlook
# 4    eve@googlemail.com      eve  googlemail

# String Length & Split
df['Name_Length'] = df['Name'].str.len()
df['Email_Split'] = df['Email'].str.split('@')
print(df[['Name', 'Name_Length', 'Email_Split']])
#     Name  Name_Length              Email_Split
# 0    alice            5  [alice, googlemail.com]
# 1      BOB            3         [bob, yahoo.com]
# 2  Charlie            7                     None
# 3    David            5     [david, outlook.com]
# 4      Eve            3    [eve, googlemail.com]

# Joining Two Columns
df['Full_Info'] = df['Name'].str.cat(df['City_Clean'], sep=' - ')
print(df[['Full_Info']])

#             Full_Info
# 0        alice - Delhi
# 1         BOB - Mumbai
# 2  Charlie - Bangalore
# 3      David - Unknown