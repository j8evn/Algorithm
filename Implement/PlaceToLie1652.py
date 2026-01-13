import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(input().strip())

c= 0
for i in range(N):
    k, t= A[i][0], 0
    for j in range(1,N):
        if k=='.' and k==A[i][j]:
            t += 1
        else:
            if t>=1:
                c += 1
            t= 0
            k= A[i][j]
    if t>=1:
        c += 1
r= 0
for i in range(N):
    k, t= A[0][i], 0
    for j in range(1,N):
        if k=='.' and k==A[j][i]:
            t += 1
        else:
            if t>=1:
                r += 1
            t= 0
            k= A[j][i]
    if t>=1:
        r += 1
print(c,r)