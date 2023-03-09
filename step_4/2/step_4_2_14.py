import csv

with open('deniro.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

