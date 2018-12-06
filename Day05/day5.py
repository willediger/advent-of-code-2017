from collections import Counter
import re

test = False
day = 5

input_path = 'Day' + format(day, '02d') + '/'
if test:
    input_path += 'test_'
input_path += 'input'

file_input = open(input_path, 'r')
file_array = file_input.read().splitlines()
file_input.close()

array_jumps = [int(l) for l in file_array]

array_jumps_len = len(array_jumps)

i = 0
steps = 0
while i < array_jumps_len:
    steps += 1
    orig_i = i
    i += array_jumps[i]
    array_jumps[orig_i] += 1

print('a', steps)

array_jumps = [int(l) for l in file_array]
i = 0
steps = 0
while i < array_jumps_len:
    steps += 1
    orig_i = i
    i += array_jumps[i]
    if array_jumps[orig_i] >= 3:
        array_jumps[orig_i] -= 1
    else:
        array_jumps[orig_i] += 1

print('b', steps)