import sys
input= sys.stdin.readline

N, L= map(int,input().split())
A= list(map(int,input().split()))
A.sort()

s, cnt= A[0]+L, 1
for i in range(N):
    if s>A[i]:
        continue
    s= A[i]+L
    cnt += 1
print(cnt)