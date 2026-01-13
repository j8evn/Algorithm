N,M=map(int,input().split())
A=list(range(1,N+1))

for i in range(M):
    r,l=map(int,input().split())
    r,l=r-1,l-1
    while(r<l):
        A[l],A[r]=A[r],A[l]
        r,l=r+1,l-1

A=list(map(str,A))
print(' '.join(A))
