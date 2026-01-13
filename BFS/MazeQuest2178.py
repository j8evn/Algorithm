from collections import deque

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
    cnt= 0
    while que:
        ll= len(que)
        cnt += 1
        for _ in range(ll):
            r, c= que.popleft()
            if r==M-1 and c==N-1:
                return cnt
            for i in range(4):
                nr, nc= r+dir[i][0], c+dir[i][1]
                if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]=='1'):
                    V[nr][nc]= True
                    que.append((nr,nc))
    return False

M, N= map(int,input().split())
A= []
for i in range(M):
    A.append(input())

V= []
for i in range(M):
    V.append([False]*N)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

print(bfs(0,0))
