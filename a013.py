def roma(roma):
    dic = {"I" : 1, "V" : 5, "X" : 10,
        "L" : 50, "C" : 100, "D" : 500,
        "M" : 1000}
    result = 0
    for i in range(len(roma)-1):
        now = dic[roma[i]]
        new = dic[roma[i+1]]
        if now > new:
            result -= now
        else:
            result += now
    result += dic[roma[-1]]
    return result

def number(romaa):
    dic = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
    50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1:"I" }
    if romaa == 0:
        return 'ZERO'
    
    result = ""
    for key , value in dic.items():
        while romaa - key >= 0:
            romaa -= key
            result += value
    return result


inp = input()
while inp != "#":
    roma_a , roma_b = inp.split()
    romasum_a , romasum_b = roma(roma_a) , roma(roma_b)
    roma_ans = abs(romasum_a - romasum_b)
    ans = number(roma_ans)
    print(ans)
    inp = input()