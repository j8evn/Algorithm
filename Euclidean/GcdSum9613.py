def gcd(a,b):
    if (a<b):
        a,b=b,a
    while True:
        if (a%b==0):
            return b
        a,b=b,a%b

t= int(input())
for _ in range(t):
    A= list(map(int,input().split()))
    A.pop(0)
    S= 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            S += gcd(A[i],A[j])
    print(S)