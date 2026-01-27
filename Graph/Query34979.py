import sys
input= sys.stdin.readline

N, Q= map(int,input().split())
G= [[0]*N for _ in range(4)]

for _ in range(Q):
    q= list(map(int,input().split()))

    if q[0]==1:
        a, b= q[1], q[2]
        G[a-1][b-1] += 1
        
        if b-2 >= 0:
            G[a-1][b-2] += 1
        if b < N:
            G[a-1][b] += 1
        if a-2 >= 0:
            G[a-2][b-1] += 1
        if a < 4:
            G[a][b-1] += 1

    elif q[0]==2:
        a= q[1]
        mm, idx= -1, 0
        for i in range(N):
            if G[a-1][i] > mm:
                mm= G[a-1][i]
                idx= i+1
        print(idx)

mm, f, idx= -1, 0, 0
for i in range(4):
    for j in range(N):
        if G[i][j] > mm:
            mm= G[i][j]
            f= i+1
            idx= j+1
print(f, idx)