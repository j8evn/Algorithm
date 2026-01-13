import sys
input= sys.stdin.readline

def Valid(r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs(x,y):
    que, fr= [], 0
    que.append([x,y])
    V = [[False] * N for _ in range(M)]
    V[x][y]= True
    cnt= 0
    while (len(que)>fr):
        ll= len(que)-fr
        cnt += 1
        for j in range(ll):
            r, c= que[fr][0], que[fr][1]
            fr += 1
            for i in range(4):
                nr, nc= r+dir[i][0], c+dir[i][1]
                if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]=='L'):
                    V[nr][nc]= True
                    que.append([nr,nc])
    return cnt-1

dir= [[-1,0],[1,0],[0,-1],[0,1]]

M, N= map(int,input().split())
A= []
for i in range(M):
    A.append(input())

L= []
for i in range(M):
    for j in range(N):
        if A[i][j]=='L':
            L.append([i,j])

R= 0
for i in range(len(L)):
    R= max(R,bfs(L[i][0],L[i][1]))
print(R)