N,M=map(int,input().split())
A=[0]*N
for i in range(M):
    a,b,k=map(int,input().split())
    for j in range(a-1,b):
        A[j]=k
A=list(map(str,A))
print(' '.join(A))
