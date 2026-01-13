import sys
input= sys.stdin.readline

N, M= map(int,input().split())
B= []
for i in range(N):
    B.append(i+1)

for _ in range(M):
    i, j, k= map(int,input().split())
    tt= B[i-1:j]
    while tt[0]!=B[k-1]:
        tt.append(tt.pop(0))
    B[i-1:j]= tt
print(*B)