import sys
input= sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
B= list(map(int,input().split()))
A.sort(reverse=True)
B.sort()
for i in range(N):
    A[i]= A[i]*B[i]
print(sum(A))