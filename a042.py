while True:
    try:
        inp = int(input())
        if inp == 1:
            print(2)
        else:
            sum = inp ** 2 - inp + 2
            print(sum)
    except EOFError:
        break