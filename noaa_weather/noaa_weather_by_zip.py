import csv

with open('2219354_custom_ghcn_daily.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(', '.join(row))
