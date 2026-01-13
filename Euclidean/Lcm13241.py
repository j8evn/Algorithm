def gcd(a,b):
    if (a<b):
        a, b= b, a
    while True:
        if (a%b==0):
            return b
        a, b= b, a%b

A, B= map(int,input().split())
g= gcd(A,B)
print((A//g)*(B//g)*g)