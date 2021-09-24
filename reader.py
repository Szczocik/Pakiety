import os
import sys
import pprint

data = [
    ['Adam', '1', 'Nowak'],
    ['Tomek', '3', 'Kowalski'],
    ['Ada', '4', 'Nowak']
]


input_filename = sys.argv[1:][0]
output_filename = sys.argv[1:][1]
changes = sys.argv[1:][2:]
print(input_filename)
print(output_filename)
print(changes)
