import sys
input= sys.stdin.readline

N= int(input())
G= []
for i in range(N):
    G.append(list(input().split()))
    G[i][1:4]= map(int,G[i][1:4])
G.sort(key=lambda x:x[0])
G.sort(key=lambda x:-x[3])
G.sort(key=lambda x:x[2])
G.sort(key=lambda x:-x[1])

R= []
for i in range(N):
    R.append(G[i][0])
print("\n".join(R))