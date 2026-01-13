import sys
input= sys.stdin.readline

N= int(input())
C, G= [0]*N, [[] for _ in range(N)]
tt= []
for i in range(N):
    k= list(map(int,input().split()))
    tt.append(k[0])
    for j in range(k[1]):
        G[k[2+j]-1].append(i)
        C[i]= C[i]+1

dp= [0]*N
Q, front, rear= [0]*N, 0, 0
for i in range(N):
    if C[i]==0:
        Q[rear], rear= i, rear+1
        dp[i]= tt[i]
while front<rear:
    n, front= Q[front], front+1
    for t in G[n]:
        dp[t]= max(dp[t],dp[n]+tt[t])
        C[t]= C[t]-1
        if C[t]==0:
            Q[rear], rear= t, rear+1
print(max(dp))