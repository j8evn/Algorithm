import sys
input= sys.stdin.readline

def Valid(h,r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=N:
        return False
    if h<0 or h>=H:
        return False
    return True

def bfs():
    fr= 0
    cnt= 0
    while (len(que)>fr):
        ll= len(que)-fr
        cnt += 1
        for j in range(ll):
            h, r, c= que[fr][0], que[fr][1], que[fr][2]
            fr += 1
            for i in range(6):
                nh, nr, nc= h+dir[i][2], r+dir[i][0], c+dir[i][1]
                if (Valid(nh,nr,nc)==True) and (V[nh][nr][nc]==False) and (A[nh][nr][nc]==0):
                    V[nh][nr][nc]= True
                    A[nh][nr][nc]= 1
                    que.append([nh,nr,nc])
    return cnt

N, M, H= map(int,input().split())
check1= True
A= []
for _ in range(H):
    a= []
    for i in range(M):
        a.append(list(map(int,input().split())))
        if 0 in a[i]:
            check1= False
    A.append(a)

V=[]
for _ in range(H):
    a= []
    for _ in range(M):
        a.append([False]*N)
    V.append(a)

dir= [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[-1,0,0],[1,0,0]]

que= []
for k in range(H):
    for i in range(M):
        for j in range(N):
            if A[k][i][j]==1:
                que.append([k,i,j])
                V[k][i][j]= True
R= bfs()
check2= True
for k in range(H):
    for i in range(M):
        for j in range(N):
            if A[k][i][j]==0:
                check2= False

if check1==True:
    print(0)
elif check2==True:
    print(R-1)
else:
    print(-1)