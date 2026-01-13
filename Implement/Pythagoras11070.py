import sys
input= sys.stdin.readline

t= int(input())
for i in range(t):
    n, m= map(int,input().split())
    S= [[0]*n,[0]*n]
    for j in range(m):
        a, b, p, q= map(int,input().split())
        S[0][a-1] += p
        S[1][a-1] += q
        S[0][b-1] += q
        S[1][b-1] += p
    W= [0]*n
    for j in range(n):
        if (S[0][j]+S[1][j]==0):
            W[j]= 0
        else:
            W[j]=int((S[0][j]**2)/(S[0][j]**2+S[1][j]**2)*1000)
    print(max(W))
    print(min(W))
