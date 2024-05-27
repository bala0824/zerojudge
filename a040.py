
def loop(a, b):
    all = ""
    for i in range(a,b+1):
        i = str(i)
        p = len(i)
        result = 0
        for x in range(len(i)):
            result += int(i[x]) ** p
            if p-1 == int(x) and result == int(i):
                all += str(result) + " "
                break
    return all

a,b = map(int,input().split())
sum = loop(a,b)
if sum == "":
    print("none")
else:
    print(sum)