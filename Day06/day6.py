from collections import Counter
import re

test = False
day = 6

input_path = 'Day' + format(day, '02d') + '/'
if test:
    input_path += 'test_'
input_path += 'input'

file_input = open(input_path, 'r')
file_array = file_input.read().splitlines()
file_input.close()

banks = [int(e) for e in file_array[0].split('\t')]
bank_count = len(banks)

bank_history = []
bank_history.append(list(banks)) #wrapped banks with list() to avoid changes later on to be perpetuated in bank_history

x = banks in bank_history

seen_before = False
steps = 0
while not seen_before:
    blocks_to_redistribute = max(banks)
    block_id = banks.index(blocks_to_redistribute)
    banks[block_id] = 0
    steps += 1
    while blocks_to_redistribute > 0:
        if block_id == bank_count - 1:
            block_id = 0
        else:
            block_id += 1
        banks[block_id] += 1
        blocks_to_redistribute -= 1
    seen_before = banks in bank_history
    bank_history.append(list(banks))

print('a', steps)

last_bank = len(bank_history) - 1
repeated = bank_history[last_bank]

first = bank_history.index(repeated)

print('b', last_bank - first)