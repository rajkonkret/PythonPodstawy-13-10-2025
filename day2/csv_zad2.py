import csv

fields = []
rows = []

filename = 'recordc_dict.csv'
with open(filename, "r") as csv_f:
    csvreader = csv.reader(csv_f)

    print(csvreader)  # <_csv.reader object at 0x0000027509C0BFA0>, iterator

    fields = next(csvreader)  # odczyta pierwszy wiersz, ustawi odczyt na nastepny

    for row in csvreader:  # odczyt od drugiego wiersza, działa iterator
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'coe']
# Rows: [['Radek', 'coe', '3', '90']]