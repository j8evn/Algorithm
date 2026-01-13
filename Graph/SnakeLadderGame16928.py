from collections import deque
import sys
input= sys.stdin.readline

def bfs(n):
    que= deque()
    que.append(n)
    V[n]= True
    ans= 0
    while que:
        ll= len(que)
        for _ in range(ll):
            nn= que.popleft()
            if nn==100:
                return ans
            for i in range(1,7):
                if nn+i<=100 and V[nn+i]==False:
                    V[nn+i]= True
                    if G[nn+i]!=-1:
                        que.append(G[nn+i])
                        V[G[nn+i]]= True
                    else:
                        que.append(nn+i)
        ans += 1
    return ans

N, M= map(int,input().split())
V= [False]*101
G= [-1]*101
for _ in range(N+M):
    n1, n2= map(int,input().split())
    G[n1]= n2
print(bfs(1))
