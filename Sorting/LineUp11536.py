import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(input().strip())
B= sorted(A)
C= sorted(A, reverse=True)

if A==B:
    print("INCREASING")
elif A==C:
    print("DECREASING")
else:
    print("NEITHER")