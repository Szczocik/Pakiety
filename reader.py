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
        line_1 = splitted_line[2:]
        line_2 = splitted_line[3:]
        product_price = splitted_line[4:]
        data = [
            [first_line = ]
        ]

file.close()