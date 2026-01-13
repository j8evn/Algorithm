import sys
input = sys.stdin.readline

N,X=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for i in range(N-1):
    B.append(A[i]+A[i+1])
mm=min(B)
print(mm*X)
