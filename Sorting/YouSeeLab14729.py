import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(float(input()))
A.sort()
R= []
for i in range(7):
    R.append(f"{A[i]:.3f}")
print('\n'.join(R))