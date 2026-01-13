def gcd(a,b):
    if (a<b):
        a,b=b,a
    while True:
        if (a%b==0):
            return b
        a,b=b,a%b

T=int(input())
for t in range(T):
    A=list(map(int,input().split()))
    N=len(A)
    mm=-1
    for i in range(N):
        for j in range(i+1,N):
            mm=max(mm,gcd(A[i],A[j]))
    print(mm)
