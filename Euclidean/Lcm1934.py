def gcd(a,b):
    if (a<b):
        a, b= b, a
    while True:
        if (a%b==0):
            return b
        a, b= b, a%b

T= int(input())
for _ in range(T):
    a, b= map(int,input().split())
    g= gcd(a,b)
    print((a//g)*(b//g)*g)