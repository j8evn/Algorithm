import sys
input= sys.stdin.readline

N, M= map(int,input().split())
A, B= [], [[] for _ in range(M)]
score= [0]*N
for _ in range(N):
    A.append(sorted(list(map(int,input().split()))))
    for i in range(M):
        B[i].append(A[-1][i])

for i in range(N):
    for j in range(M):
        if A[i][j]==max(B[j]):
            score[i] += 1
R= []
for i in range(N):
    if score[i]==max(score):
        R.append(i+1)
print(*R)