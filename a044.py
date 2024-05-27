while True:
    try:
        n = int(input())
        sum = ((n+1)*((n*n)-n+6))/6
        print(int(sum))
    except EOFError:
        break