n = int(input())
for i in range(n):
    x , y , z , a = map(int , input().split())
    b = 0
    if y - x == z - y:
        b = a + y - x
        print(x , y , z , a , b)
    elif y / x  == z / y:
        b = a * (y / x)
        print(x , y , z , a , int(b))