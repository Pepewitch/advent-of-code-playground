from os.path import join, dirname

f = open(join(dirname(__file__), 'input.txt'))

num_set = set('0123456789')

out = 0
for line in f:
    first = ''
    last = ''
    for char in line:
        if char in num_set:
            if first == '':
                first = char
            last = char
    num = first + last
    if(num == ''):
        continue
    out += int(num)

print(out)