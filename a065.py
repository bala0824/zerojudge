inp = input()
u = 0
ans = ''
for i in range(len(inp)-1):
    sum = abs(ord(inp[u]) - ord(inp[u+1]))
    ans += str(sum)
    u += 1
print(ans)