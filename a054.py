inp = input()
u = 8
result = 0
# 前八碼總和
for x in inp: 
    result += int(x)*u
    u-=1
all = result

dic = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G",17:"H",34:"I",18:"J"
        , 19:"K",20:"L",21:"M",22:"N",35:"O",23:"P",24:"Q",25:"R",26:"S",
        27:"T",28:"U",29:"V",32:"W",30:"X",31:"Y",33:"Z"}
ans = ""
for key,value in dic.items():
    result = all
    if key < 10:
        result += key % 10 * 9 + 1
        result = 10 - (result % 10)
        if result == 10:
            result = 0
        if result == int(inp[-1]):
            ans += str(value)
    elif key < 20:
        result += key % 10 * 9 + 1
        result = 10 - (result % 10)
        if result == 10:
            result = 0
        if result == int(inp[-1]):
            ans += str(value)
    elif key < 30:
        result += key % 20 * 9 + 2
        result = 10 - (result % 10)
        if result == 10:
            result = 0
        if result == int(inp[-1]):
            ans += str(value)
    elif key < 36:
        result += key % 30 * 9 + 3
        result = 10 - (result % 10)
        if result == 10:
            result = 0
        if result == int(inp[-1]):
            ans += str(value)

print(ans)