T=int(input())
for i in range(T):
    a,b=0,0
    N=int(input())
    for i in range(N):
        C,G=map(float,input().split())
        a+=(C*G)
        b+=C
    t=a/b
    print('%d %.1f' % (b, t))
