
while True:
    try:
        y = input()
        print(*sorted([int(x) for x in input().split()]))
        
    except EOFError:
        break
