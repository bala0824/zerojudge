ini = int(input())
sum = ''
i = 1
while True:
    i += 1
    if ini % i == 0:
        x = 0
        y = ''
        z = ''
        while True:
            if ini % i == 0:
                x += 1
                ini = ini / i
                continue
            elif ini % i != 0 and x > 1:
                y = '^'
                z = ' * '
                break
            elif ini % i != 0 and x == 1:
                x = ''
                y = ' * '
                z = ''
                break
        sum += str(i) + y + str(x) + z
    elif ini == 1:
        break
last_star = sum.rfind(' * ')
sum = sum[:last_star]
print(sum)