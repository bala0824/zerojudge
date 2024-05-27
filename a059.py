inp = int(input())
u = 1
for rg in range(inp):
    result = 0
    a , b = int(input()),int(input())
    for i in range(1,b):
        if i ** 2 <= b and i ** 2 >= a:
            result += i ** 2
        elif i ** 2 > b:
            break
    print("Case "+str(u)+": "+str(result))
    u += 1