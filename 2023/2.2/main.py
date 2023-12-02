from os.path import join, dirname

f = [line for line in open(join(dirname(__file__), 'input.txt'))]

out = 0
for i in range(len(f)):
    line = f[i]
    picks = [i.strip() for i in line.strip().split(':')[1].split(';')]
    red_count = 0
    green_count = 0
    blue_count = 0
    for pick in picks:
        each_picks = [i.strip() for i in pick.split(',')]
        for each_pick in each_picks:
            num, color = each_pick.split(' ')
            num = int(num)
            if color == 'red' and num > red_count:
                red_count = num
            if color == 'green' and num > green_count:
                green_count = num
            if color == 'blue' and num > blue_count:
                blue_count = num
    out += red_count * green_count * blue_count
print(out)