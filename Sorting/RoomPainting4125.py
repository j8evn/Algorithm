import sys
input= sys.stdin.readline

n, m= map(int,input().split())
N, M= [], []
for _ in range(n):
    N.append(int(input()))
for _ in range(m):
    M.append(int(input()))
N.sort()
M.sort()

i, j= 0, 0
s= 0
while j!=m:
    if N[i]>=M[j]:
        s += (N[i]-M[j])
        j += 1
    else:
        i += 1
print(s)