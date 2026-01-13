import sys
input= sys.stdin.readline

N, K= map(int,input().split())
A= list(map(int,input().split()))
A.insert(0,0)
for i in range(N):
    A[i+1] += A[i]
B= sorted(A[1:], reverse=True)
print(sum(B[:K]))