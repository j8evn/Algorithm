import sys
sys.setrecursionlimit(100000)

def dfs(n,f):
    mm= -1
    for e in G[n]:
        if e==f:
            continue
        mm= max(mm,dfs(e,n))
    mm += 1
    D[n]= mm
    return mm

def cdfs(n,f):
    ss= 0
    for e in G[n]:
        if e==f:
            continue
        if D[e]<F:
            continue
        ss += cdfs(e,n)
    return ss+2

N, S, F= map(int,input().split())
S= S-1
G= []
D= [0]*N
for i in range(N):
    G.append([])
for i in range(N-1):
    n1, n2= map(int,input().split())
    n1, n2= n1-1, n2-1
    G[n1].append(n2)
    G[n2].append(n1)
dfs(S,-1)
print(cdfs(S,-1)-2)