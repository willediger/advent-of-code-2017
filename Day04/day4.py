from collections import Counter
import re

test = False
day = 4

input_path = 'Day' + format(day, '02d') + '/'
if test:
    input_path += 'test_'
input_path += 'input'

file_input = open(input_path, 'r')
file_array = file_input.read().splitlines()
file_input.close()

array_words = [re.findall(r'\w+', l) for l in file_array]

def word_count(word_array):
    return [Counter(l) for l in word_array]

word_counts = word_count(array_words)

def unique_phrases(word_count_arr):
    return len([v for v in [max(l.values()) for l in word_count_arr] if v == 1])

unique_passphrases = unique_phrases(word_counts)

print('a', unique_passphrases)

sorted_array_words = [[''.join(sorted(w)) for w in l] for l in array_words]
word_counts = word_count(sorted_array_words)
unique_passphrases = unique_phrases(word_counts)

print('b', unique_passphrases)