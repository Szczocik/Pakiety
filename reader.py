import os
import sys
import pprint

data_output = []

params = sys.argv[1:]

input_filename = params[0]
output_filename = params[1]
changes = params[2:]

# files = files.os.system(ls)


with open(f'{input_filename}', 'r') as file:
    for line in file:
        splitted_line = line.split(';')
        position_1 = splitted_line[0]
        position_2 = splitted_line[1]
        position_3 = splitted_line[2]
        data = [position_1, position_2, position_3.replace('\n', '')]

        data_output.append(data)
    print(data_output)

    for change in changes:
        splitted_change = change.split(',')
        y = int(splitted_change[0])
        x = int(splitted_change[1])
        value = splitted_change[2]
        data_output[x][y] = value
    print(y, x, value)

with open(f'{output_filename}', 'w') as output_filename:
    for line in data_output:
        output_filename.write(f'{line[0]}' + ';' + f'{line[1]}' + ';' + f'{line[2]}' + '\n')
        print(line)




