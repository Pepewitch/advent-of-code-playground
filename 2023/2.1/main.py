from os.path import join, dirname

f = [line for line in open(join(dirname(__file__), 'input.txt'))]

out = 0
for i in range(len(f)):
    line = f[i]
    picks = [i.strip() for i in line.strip().split(':')[1].split(';')]
    is_possible = True
    for pick in picks:
        if not is_possible:
            break
        each_picks = [i.strip() for i in pick.split(',')]
        for each_pick in each_picks:
            num, color = each_pick.split(' ')
            num = int(num)
            if color == 'red' and num > 12:
                is_possible = False
                break
            if color == 'green' and num > 13:
                is_possible = False
                break
            if color == 'blue' and num > 13:
                is_possible = False
                break
    if is_possible:
        out += i + 1
print(out)