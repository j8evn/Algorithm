def Valid(r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=M:
        return False
    return True

def bfs(S):
    fr= 0
    for _ in range(S):
        ll= len(que)-fr
        for j in range(ll):
            r, c= que[fr][0], que[fr][1]
            fr += 1
            for i in range(4):
                nr, nc= r+dir[i][0], c+dir[i][1]
                if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==0):
                    V[nr][nc]= True
                    A[nr][nc]= A[r][c]
                    que.append([nr,nc,A[nr][nc]])
    return

M, K= map(int,input().split())
A= []
for i in range(M):
    A.append(list(map(int,input().split())))
S, X, Y= map(int,input().split())

V=[]
for i in range(M):
    V.append([False]*M)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

que= []
for i in range(M):
    for j in range(M):
        if A[i][j]!=0:
            que.append([i,j,A[i][j]])
            V[i][j]= True
que.sort(key=lambda x:x[2])
bfs(S)
print(A)
print(A[X-1][Y-1])
