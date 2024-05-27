inp = int(input())
b = []
for i in range(inp):
    b.append(int(input())%3)

print(b.count(0),b.count(1),b.count(2)) 