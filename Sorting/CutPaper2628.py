import sys
input= sys.stdin.readline

N, M= map(int,input().split())
t= int(input())
A, B= [0,M], [0,N]

for _ in range(t):
    a, b= map(int,input().split())
    if a==0:
        A.append(b)
    else:
        B.append(b)
A.sort()
B.sort()

ma, mb= 0, 0
for i in range(1, len(A)):
    ma= max(ma, A[i]-A[i-1])
for i in range(1, len(B)):
    mb= max(mb, B[i]-B[i-1])
print(ma*mb)