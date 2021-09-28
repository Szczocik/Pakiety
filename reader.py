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
        data = [position_1, position_2, position_3]

        data_output.append(data)
    print(data_output)

    for change in changes:
        splitted_change = change.split(',')
        y = splitted_change[0]
        x = splitted_change[1]
        value = splitted_change[2]
    print(y, x, value)






os.mkdir(f'{output_filename}')
name = f'{output_filename}'
with open(f'{data_output}', 'w') as output_filename:
    output_filename.write(f'{position_1}' + ';' + f'{position_2}' + ';' + f'{position_3}' + '\n')
    print(data_output)




