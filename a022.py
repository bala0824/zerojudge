def eng(num):
    e = 0
    f = -1
    for i in num[e]:
        e += 1
        for x in num[f]:
            f -= 1
            if x == i:
                return "yes"
            else:
                return "no"

int = input()
print(eng(int))