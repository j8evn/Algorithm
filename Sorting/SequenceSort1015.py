import sys
input= sys.stdin.readline

n= int(input())
A= list(map(int,input().split()))
for i in range(n):
    A[i]= [A[i], i]

B= sorted(A, key=lambda x: x[0])
for i in range(n):
    B[i].append(i)
B.sort(key=lambda x: x[1])

print(' '.join(str(B[i][2]) for i in range(n)))