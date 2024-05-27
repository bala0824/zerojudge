
while True:
    try:
        inp = input()
        newinp = inp.replace("/","//")
        print(eval(newinp))
    except EOFError:
        break
