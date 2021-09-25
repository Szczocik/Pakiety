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
        position_1 = splitted_line[2:]
        position_2 = splitted_line[3:]
        position_3 = splitted_line[4:]
        data = [position_1, position_2, position_3]


file.close()

# file = open('baza_danych.txt', 'w')
#         file.write('saldo:' + str(saldo) + '\n')
#         for product_name, data in store.items():
#             file.write(str(product_name) + ';' + str(data['count']) + ';' + str(data['price']) + '\n')
#         file.close()