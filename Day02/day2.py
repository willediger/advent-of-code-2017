file_input = open('Day02/input', 'r')
file_array = file_input.read().splitlines()

while file_array != [l.replace('  ', ' ') for l in file_array] or file_array != [l.replace('\t', ' ') for l in file_array]:
    file_array = [l.replace('  ', ' ') for l in file_array]
    file_array = [l.replace('\t', ' ') for l in file_array]

file_array_list = [l.split(' ') for l in file_array]
file_array_list_ints = [[int(i) for i in l] for l in file_array_list]
file_array_checksum = [max(l)-min(l) for l in file_array_list_ints]
file_checksum = sum(file_array_checksum)

print('a', file_checksum)

file_array_checksum = []
for i in range(0, len(file_array_list_ints)):
    list_i = file_array_list_ints[i]
    i_len = len(list_i)
    for j in range(0, i_len):
        for k in range(0, i_len):
            if int(list_i[j] % list_i[k]) == 0 and j != k:
                file_array_checksum.append(int(list_i[j]/list_i[k]))

file_checksum = sum(file_array_checksum)

print('b', file_checksum)