import sys
input= sys.stdin.readline

N, M= map(int,input().split())
D= {}
for _ in range(N):
    ss= input().strip()
    D[ss]= 1
for _ in range(M):
    ss= input().strip()
    if ss in D:
        D[ss] += 1
    else:
        D[ss]= 1

R= []
for d in D:
    if D[d]==2:
        R.append(d)
R.sort()
print(len(R))
print('\n'.join(R))