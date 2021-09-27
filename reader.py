import os
import sys
import pprint

data_output = []

params = sys.argv[1:]

input_filename = params[0]
output_filename = params[1]
# changes = params[2:]
# print(input_filename)
# print(output_filename)
# print(changes)
# files = files.os.system(ls)


with open(f'{input_filename}', 'r') as file:
    for line in file:
        splitted_line = line.split(';')
        position_1 = splitted_line[0]
        position_2 = splitted_line[1]
        position_3 = splitted_line[2]
        data = [position_1, position_2, position_3]

        data_output.append(data)
        print(data)


    print(data_output)

with open(f'{input_filename}', 'w') as output_filename:
    output_filename.write()

file = open('baza_danych.txt', 'w')
        file.write('saldo:' + str(saldo) + '\n')
        for product_name, data in store.items():
            file.write(str(product_name) + ';' + str(data['count']) + ';' + str(data['price']) + '\n')
        file.close()


