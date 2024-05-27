while True:
    try:
        inp = int(input())
        print(bin(inp)[2:])
    except EOFError:
        break