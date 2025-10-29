import pandas as pd

data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Order_Date': ['2023-01-05', '2023/02/10', '2023-03-15', '15-04-2023', '2023.05.20'],
    'Amount': [2500, 1800, 2100, 1900, 3000]
}

df = pd.DataFrame(data)
print(df)
#    Order_ID  Order_Date  Amount
# 0       101  2023-01-05    2500
# 1       102  2023/02/10    1800
# 2       103  2023-03-15    2100
# 3       104  15-04-2023    1900
# 4       105  2023.05.20    3000

df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='mixed')
print(df)
#    Order_ID Order_Date  Amount
# 0       101 2023-01-05    2500
# 1       102 2023-02-10    1800
# 2       103 2023-03-15    2100
# 3       104 2023-04-15    1900
# 4       105 2023-05-20    3000

df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Day'] = df['Order_Date'].dt.day
df['Weekday'] = df['Order_Date'].dt.day_name()
print(df)
#   Order_ID Order_Date  Amount  Year  Month  Day    Weekday
# 0       101 2023-01-05    2500  2023      1    5   Thursday
# 1       102 2023-02-10    1800  2023      2   10     Friday
# 2       103 2023-03-15    2100  2023      3   15  Wednesday
# 3       104 2023-04-15    1900  2023      4   15   Saturday
# 4       105 2023-05-20    3000  2023      5   20   Saturday

# Filtering Based on Dates
df_filtered = df[df['Order_Date'] > '2023-03-01']
print(df_filtered)
#   Order_ID Order_Date  Amount  Year  Month  Day    Weekday
# 2       103 2023-03-15    2100  2023      3   15  Wednesday
# 3       104 2023-04-15    1900  2023      4   15   Saturday
# 4       105 2023-05-20    3000  2023      5   20   Saturday

# Sorting by Date
df.sort_values('Order_Date', inplace=True)
print(df)
#    Order_ID Order_Date  Amount  Year  Month  Day    Weekday
# 0       101 2023-01-05    2500  2023      1    5   Thursday
# 1       102 2023-02-10    1800  2023      2   10     Friday
# 2       103 2023-03-15    2100  2023      3   15  Wednesday
# 3       104 2023-04-15    1900  2023      4   15   Saturday
# 4       105 2023-05-20    3000  2023      5   20   Saturday

# Date Differences (Timedelta)
df['Delivery_Date'] = df['Order_Date'] + pd.to_timedelta(5, unit='d')
df['Days_Taken'] = (df['Delivery_Date'] - df['Order_Date']).dt.days
print(df)
#    Order_ID Order_Date  Amount  Year  Month  Day    Weekday Delivery_Date  Days_Taken
# 0       101 2023-01-05    2500  2023      1    5   Thursday    2023-01-10           5
# 1       102 2023-02-10    1800  2023      2   10     Friday    2023-02-15           5
# 2       103 2023-03-15    2100  2023      3   15  Wednesday    2023-03-20           5
# 3       104 2023-04-15    1900  2023      4   15   Saturday    2023-04-20           5
# 4       105 2023-05-20    3000  2023      5   20   Saturday    2023-05-25           5

# Generate Date Ranges
dates = pd.date_range(start='2023-01-01', end='2023-01-10')
print(dates)
# DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
#                '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
#                '2023-01-09', '2023-01-10'],
#               dtype='datetime64[ns]', freq='D')

# Resampling (For Time Series)
# Create daily data
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
df = pd.DataFrame({'Date': date_rng, 'Sales': [100,120,80,90,110,95,105,125,130,115]})
df.set_index('Date', inplace=True)

# Weekly summary
print(df.resample('W').sum())