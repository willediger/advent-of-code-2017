file_input = open('Day01/input', 'r')
file_array = file_input.read().splitlines()

file_str = file_array[0]
file_str_len = len(file_str)

captcha_sum = 0
for i, c in enumerate(file_str):
    c_int = int(c)
    if i == file_str_len - 1:
        c_next = file_str[0]
    else:
        c_next = file_str[i+1]
    c_next = int(c_next)
    if c_int == c_next:
        captcha_sum += c_int

print(captcha_sum)
