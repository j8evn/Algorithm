from collections import deque

def Valid(r,c):
    if r<0 or r>=M: # 행 범위 벗어남
        return False
    if c<0 or c>=N: # 열 범위 벗어남
        return False
    return True

def bfs(r,c):
    que= deque()
    que.append((r,c)) # 시작 좌표
    V[r][c]= True
    while que:
        r, c= que.popleft()
        if r==M-1: # 현재 좌표가 맨 아래 행에 도달하면
            return True
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]=='0'):
                V[nr][nc]= True
                que.append((nr,nc))
    return False

M, N= map(int,input().split())
A= []
for i in range(M):
    A.append(input())

V= []
for _ in range(M):
    V.append([False]*N)

dir= [[-1,0],[1,0],[0,-1],[0,1]] # 왼쪽, 오른쪽, 아래, 위

found= False
for i in range(N):
    if (A[0][i]=='0') and (V[0][i]==False):
        res= bfs(0,i)
        if res==True:
            found= True
            break
if found==True:
    print("YES")
else:
    print("NO")