while True:
    try :
        a , b = input().split()
        if a == b:
            print(int(a))
        else :
            print(int(b)+1)
    except EOFError :
        break