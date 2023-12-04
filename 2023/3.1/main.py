from os.path import join, dirname

f = [list('.' + line.strip() + '.')  for line in open(join(dirname(__file__), 'input.txt'))]

cur = ''
out = 0
num_set = set('0123456789')
adjacent_set = set('0123456789.')

for i in range(len(f)):
    for j in range(len(f[i])):
        char = f[i][j]
        if char in num_set:
            cur += char
        else:
            if cur != '':
                is_surrounded = True
                
                # check surrounded
                for k in range(len(cur)):
                    if not is_surrounded:
                        break
                    if k == 0: # need check right, top right and bottom right
                        if j < len(f[i]) and f[i][j] not in adjacent_set:
                            is_surrounded = False
                        if i - 1 >= 0 and j < len(f[i]) and f[i - 1][j] not in adjacent_set:
                            is_surrounded = False
                        if i + 1 < len(f) and j < len(f[i]) and f[i + 1][j] not in adjacent_set:
                            is_surrounded = False
                    elif k == len(cur) - 1: # need check left, top left and bottom left
                        if j - k - 2 >= 0 and f[i][j - k - 2] not in adjacent_set:
                            is_surrounded = False
                        if i - 1 >= 0 and j - k - 2 >= 0 and f[i - 1][j - k - 2] not in adjacent_set:
                            is_surrounded = False
                        if i + 1 < len(f) and j - k - 2 >= 0 and f[i + 1][j - k - 2] not in adjacent_set:
                            is_surrounded = False
                    # check up and down
                    if i - 1 >= 0 and f[i - 1][j - k - 1] not in adjacent_set:
                        is_surrounded = False
                    if i + 1 < len(f) and f[i + 1][j - k - 1] not in adjacent_set:
                        is_surrounded = False

                if not is_surrounded:
                    out += int(cur)
                cur = ''
print(out)