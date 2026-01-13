def Valid(r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs(r,c):
    que, fr= [], 0
    que.append([r,c])
    V[r][c]= True
    cnt= 1
    while (len(que)>fr):
        r, c= que[fr][0], que[fr][1]
        fr += 1
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==1):
                V[nr][nc]= True
                que.append([nr,nc])
                cnt += 1
    return cnt

M, N, K= map(int,input().split())
A= []
for i in range(M):
    A.append([0]*N)
for i in range(K):
    r, c= map(int,input().split())
    A[r-1][c-1]= 1

V=[]
for i in range(M):
    V.append([False]*N)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

R= []
for i in range(M):
    for j in range(N):
        if V[i][j]==False and A[i][j]==1:
            R.append(bfs(i,j))
print(max(R))