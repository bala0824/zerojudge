inp = int(input())
result = 0
for x in range(0,inp+1):
    if inp >= 40:
        result = 100
        break
    elif inp == 0:
        result = 0
        break
    elif x > 0 and x <= 10:
        result+=6
    elif x > 10 and x <= 20:
        result+=2
    elif x >20 and x <= 40:
        result += 1
print(result)
