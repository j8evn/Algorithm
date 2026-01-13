import sys
sys.setrecursionlimit(10000)

def Seq(f, t):
    if (f==t):
        return 0
    if (dp[f][t] != -1):
        return dp[f][t]
    mm = 10000000000
    for i in range(f, t):
        u = Seq(f, i)+Seq(i+1, t) + P[f-1]*P[i]*P[t]
        mm = min(mm, u)
    dp[f][t] = mm
    return mm

N= int(input())
P= []
for i in range(N):
    a, b= map(int,input().split())
    P.append(a)
P.append(b)

dp = []
for i in range(N+1):
    dp.append([-1]*(N+1))
print(Seq(1,N))