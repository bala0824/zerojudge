import cmath
a , b , c = map(int,input().split())
n1 = (-b + cmath.sqrt(b**2 - 4 * a * c)) / (2*a)
n2 = (-b - cmath.sqrt(b**2 - 4 * a * c)) / (2*a)
x1 = int(max(n1.real,n2.real))
x2 = int(min(n1.real,n2.real))
if b**2 - 4*a*c > 0:
    print('Two different roots x1='+str(x1)+' , x2='+str(x2))
elif b**2 - 4*a*c == 0:
    print('Two same roots x='+ str(x1))
elif b**2 - 4*a*c < 0:
    print('No real root')


