import sys
sys.setrecursionlimit(100000) # 재귀 한도 설정 (default: 1000)

def dfs(n):
    #print(n)
    for e in G[n]:
        if P[e]==-1:
            P[e]= n
            dfs(e)

N= int(input())
G= []
for i in range(N):
    G.append([])
for i in range(N-1):
    n1, n2= map(int,input().split())
    n1, n2= n1-1, n2-1
    G[n1].append(n2)
    G[n2].append(n1)
P= [-1]*N
P[0]= 100000
dfs(0)

for i in range(1,N):
    P[i] += 1
P= list(map(str,P[1:]))
print('\n'.join(P))