import sys
input= sys.stdin.readline

N= int(input())
A= [0]
for _ in range(N):
    A.append(sum(list(map(int,input().split()))[1:]))
A.sort()

for i in range(N):
    A[i+1]= A[i]+A[i+1]
print(sum(A))