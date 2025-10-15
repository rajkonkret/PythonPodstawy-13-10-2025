import pandas as pd

excel_data = pd.read_excel('sales.xlsx')
print(excel_data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

data = pd.DataFrame(excel_data)
print(data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000
print(data.columns)
# Index(['Sales Date', 'Sales Person', 'Amount'], dtype='object')

# filtrowanie danych
print(data[data['Amount'] > 45000])
#   Sales Date Sales Person  Amount
# 0 2018-05-12   Sila Ahmed   60000
# 1 2019-12-06  Mir Hossain   50000
data.to_excel("nowy_excel.xlsx")

data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 3 columns):
#  #   Column        Non-Null Count  Dtype
# ---  ------        --------------  -----
#  0   Sales Date    4 non-null      datetime64[ns]
#  1   Sales Person  4 non-null      object
#  2   Amount        4 non-null      int64
# dtypes: datetime64[ns](1), int64(1), object(1)
# memory usage: 228.0+ bytes
