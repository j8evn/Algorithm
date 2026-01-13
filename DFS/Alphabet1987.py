def Valid(r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=N:
        return False
    return True

def dfs(r,c,V,d):
    global dist
    dist= max(dist,d)
    V[ord(A[r][c])-ord('A')]= True
    check= 0
    for i in range(4):
        nr, nc= r+dir[i][0], c+dir[i][1]
        if Valid(nr,nc)==True and V[ord(A[nr][nc])-ord('A')]==False:
            check += 1
            dfs (nr,nc,V,d+1)
            V[ord(A[nr][nc])-ord('A')]= False

M, N= map(int,input().split())
A= []
for i in range(M):
    A.append(input().strip())

V= [False]*26

dir= [[-1,0],[1,0],[0,-1],[0,1]]

dist= 0
dfs(0,0,V,1)
print(dist)