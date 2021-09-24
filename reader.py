import os
import sys
import pprint

data = [
    ['Adam', '1', 'Kowalski'],
    ['Marta', '2', 'Wacha'],
    ['Sebastian', '3', 'Kostka']
]

params = sys.argv[1:]
print(params)
input_filename = params[0]
output_filename = params[1]
changes = params[2:]
print(input_filename)
print(output_filename)
print(changes)

file = open('data.csv', 'r')
for line in file.readlines():
        splitted_line = line.split(';')
        product_name = splitted_line[0]
        product_count = splitted_line[1]
        product_price = splitted_line[2]
        data = []

file.close()