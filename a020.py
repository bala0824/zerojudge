def name(num):
    dic = {"A" : 10 , "B" : 11 , "C" : 12 , "D" : 13 , "E" : 14,
        "F" : 15 , "G" : 16 , "H" : 17 , "J" : 18 , "K" : 19,
        "L" : 20 , "M" : 21 , "N" : 22 , "P" : 23 , "Q" : 24,
        "R" : 25 , "S" : 26 , "T" : 27 , "U" : 28 , "V" : 29,
        "X" : 30 , "Y" : 31 , "W" : 32 , "Z" : 33 , "I" : 34,
        "O" : 35}
    result = 0
    y = dic[num[0]]
    if y < 20:
        result += 1
        p = y % 10 
    elif y < 30 and y >= 20:
        result +=  2
        p = y % 20 
    elif y <= 35 and y >= 30:
        result +=  3
        p = y % 30
    result += p * 9
    u = 8
    for i in num[1:10]:
        result += int(i) * u
        if u == 0:
            result += int(i)
        u -= 1

    if result % 10 == 0:
        return "real"
    else:
        return "fake"



inp = input()
print(name(inp))