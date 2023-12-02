from os.path import join, dirname
import re

f = open(join(dirname(__file__), 'input.txt'))

num_set = set('0123456789')
num_string_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

out = 0
for line in f:
    first = ''
    first_index = -1
    last = ''
    last_index = -1

    for index in range(len(line)):
        char = line[index]
        if char in num_set:
            if first == '':
                first = char
                first_index = index
            last = char
            last_index = index
    for key in num_string_map:
        start_list = [i.start() for i in re.finditer(key, line)]
        if len(start_list) == 0:
            continue
        if first_index > start_list[0]:
            first = num_string_map[key]
            first_index = start_list[0]
        if last_index < start_list[-1]:
            last = num_string_map[key]
            last_index = start_list[-1]

    num = first + last
    if(num == ''):
        continue
    out += int(num)

print(out)