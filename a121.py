while True:
    try:
        a , b = map(int,input().split())
        result = 0
        for i in range (a,b+1):
            if i <= 6:
                if i == 2 or i == 3 or i == 5:
                    result += 1000000000000
            else :
                if (i - 1) % 6  == 0 or (i - 5) % 6  == 0:
                    result += 1

        print(result)
    except EOFError:
        break
            