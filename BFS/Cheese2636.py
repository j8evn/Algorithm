from collections import deque
import sys
input= sys.stdin.readline

def Valid(r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs(x,y):
    que= deque()
    que.append((x,y))
    V[x][y]= True
    while que:                                                                      
        r, c= que.popleft()
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False):
                V[nr][nc]= True
                if A[nr][nc]==0:
                    que.append((nr,nc))
                elif A[nr][nc]==1:
                    melt.append((nr,nc))
    for x, y in melt:
        A[x][y]= 0
    return len(melt)

M, N= map(int,input().split())
A= []
for _ in range(M):
    A.append(list(map(int,input().split())))
V= []
for i in range(M):
    V.append([False]*N)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

total= 0
for i in range(M):
    total += A[i].count(1)
melt= []
cnt= bfs(0,0)
total -= cnt
t= 1
while total>0:
    t += 1
    V= []
    for i in range(M):
        V.append([False]*N)
    melt= []
    cnt= bfs(0,0)
    total -= cnt
print(t)
print(cnt)