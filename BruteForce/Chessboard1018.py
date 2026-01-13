import copy
import sys
input= sys.stdin.readline

N, M= map(int,input().split())
B= []
for _ in range(N):
    B.append(list(input().strip()))

R= []
for i in range(N-7):
    for j in range(M-7):
        d1= 0
        d2= 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if B[a][b]!='B':
                        d1 += 1
                    if B[a][b]!='W':
                        d2 += 1
                else:
                    if B[a][b]!='W':
                        d1 += 1
                    if B[a][b]!='B':
                        d2 += 1
        R.append(d1)
        R.append(d2)
print(min(R))