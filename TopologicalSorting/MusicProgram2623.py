import sys
input= sys.stdin.readline

N, M= map(int,input().split())
C, G= [0]*N, [[] for _ in range(N)]
for _ in range(M):
    k= list(map(int,input().split()))
    for i in range(1,k[0]):
        G[k[i]-1].append(k[i+1]-1)
        C[k[i+1]-1]= C[k[i+1]-1]+1

Q, front, rear= [0]*N, 0, 0
for i in range(N):
    if C[i]==0:
        Q[rear], rear= i, rear+1

R= []
while front<rear:
    n, front= Q[front], front+1
    R.append(n+1)
    for t in G[n]:
        C[t]= C[t]-1
        if C[t]==0:
            Q[rear], rear= t, rear+1
if len(R)==N:
    R= map(str,R)
    print('\n'.join(R))
else:
    print(0)