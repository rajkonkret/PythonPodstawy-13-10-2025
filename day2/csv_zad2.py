import csv

fields = []
rows = []

# filename = 'recordc_dict.csv'
filename = 'discount_dane.csv'
with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "
    print(dialect.escapechar)  # None
    # ustawiamy ponownie odczyt na początek pliku
    csv_f.seek(0)

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x0000027509C0BFA0>, iterator

    fields = next(csvreader)  # odczyta pierwszy wiersz, ustawi odczyt na nastepny

    for row in csvreader:  # odczyt od drugiego wiersza, działa iterator
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'coe']
# Rows: [['Radek', 'coe', '3', '90']]

# Fields: ['sku;exp_date;price']
# Rows: [['1;today;200'],
# ['2;today;100'],
# ['3;tomorrow;200.5'],
# ['4;today;500'],
# ['5;today;99.99']]
#
# Process finished with exit code 0

# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '200'],
# ['2', 'today', '100'],
# ['3', 'tomorrow', '200.5'],
# ['4', 'today', '500'],
# ['5', 'today', '99.99']]
