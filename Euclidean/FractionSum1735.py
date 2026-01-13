def gcd(a,b):
    if (a<b):
        a, b= b, a
    while True:
        if (a%b==0):
            return b
        a, b= b, a%b

A, B= map(int,input().split())
C, D= map(int,input().split())
g= gcd(B,D)
x= (B//g)*(D//g)*g
y= A*(D//g) + C*(B//g)
print(y//gcd(y,x),x//gcd(y,x))