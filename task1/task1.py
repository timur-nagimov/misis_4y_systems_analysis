import csv

i = 5
j = 3

with open('file.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    for row_number, row in enumerate(csvreader, start=1):
        if row_number == i:
            element = row[j - 1]
            print(f'На позиции ({i}, {j}): {element}')
            break
