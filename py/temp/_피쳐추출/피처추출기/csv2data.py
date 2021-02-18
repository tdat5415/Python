import csv

with open('./features.csv', 'r') as raw:
    lines = raw.readlines()

cooked = csv.reader(lines)
for record in cooked:
    print(record)
