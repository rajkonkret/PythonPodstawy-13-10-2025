import pandas

# pip install pandas

# data = pandas.read_csv('records.csv', delimiter=",")
data = pandas.read_csv('discount_dane.csv', delimiter=";")
print(data)
#    sku  exp_date   price
# 0    1     today  200.00
# 1    2     today  100.00
# 2    3  tomorrow  200.50
# 3    4     today  500.00
# 4    5     today   99.99

print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
# [[1 'today' 200.0]
#  [2 'today' 100.0]
#  [3 'tomorrow' 200.5]
#  [4 'today' 500.0]
#  [5 'today' 99.99]]

print(data.items)
# <bound method DataFrame.items of    sku  exp_date   price
# 0    1     today  200.00
# 1    2     today  100.00
# 2    3  tomorrow  200.50
# 3    4     today  500.00
# 4    5     today   99.99>

print(data.values[0])  # [1 'today' 200.0]
print(type(data.values))  # <class 'numpy.ndarray'>
