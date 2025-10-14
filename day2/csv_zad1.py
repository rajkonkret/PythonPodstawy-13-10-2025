# pliki csv
# Name,Email,Phone Number,Address
# Bob Smith,bob@example.com,123-456-7890,123 Fake Street
# Mike Jones,mike@example.com,098-765-4321,321 Fake Avenue
# dane oddzielone zankiem podziału: ,;tab

import csv

fields = ['name', 'branch', 'year', 'coe']
row = ["Radek", "coe", "3", 90]

dict_list = dict(zip(fields, row))
print(dict_list)
# {'name': 'Radek', 'branch': 'coe', 'year': '3', 'coe': 90}

filename = 'records.csv'
# newline="" - obejscie problemu pustych linii
with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = "recordc_dict.csv"
with open(filename, "w", newline="") as fh:
    csvwriter = csv.DictWriter(fh, fieldnames=fields)
    csvwriter.writeheader()  # zapisz nagłówek (nazwy kolumn)
    csvwriter.writerow(dict_list)

products = [
    {"sku": 1, "exp_date": "today", "price": 200},
    {"sku": 2, "exp_date": "today", "price": 100},
    {"sku": 3, "exp_date": "tomorrow", "price": 200.50},
    {"sku": 4, "exp_date": "today", "price": 500},
    {"sku": 5, "exp_date": "today", "price": 99.99},
]

# list comprehensions
fields_list = [j for j in products[0]]
print(fields_list)  # ['sku', 'exp_date', 'price']

filename = "discount_dane.csv"
with open(filename, "w", newline="") as fh:
    csvwriter = csv.DictWriter(fh, fieldnames=fields_list, delimiter=";")
    csvwriter.writeheader()  # zapisz nagłówek (nazwy kolumn)
    csvwriter.writerows(products)  # writerows
