import sys
input= sys.stdin.readline

m, n= map(int,input().split())
A= [[0]*(n+1)]
for _ in range(m):
    t= list(map(int,input().split()))
    t.insert(0,0)
    A.append(t)

for i in range(1,m+1):
    for j in range(1,n+1):
        A[i][j] += A[i-1][j]+ A[i][j-1]- A[i-1][j-1]

cnt= 0
for i in range(1,m+1):
    for j in range(1,n+1):
        for a in range(i,m+1):
            for b in range(j,n+1):
                s= A[a][b]-A[a][j-1]-A[i-1][b]+A[i-1][j-1]
                if s==10:
                    cnt += 1
                if s>=10:
                    break
print(cnt)