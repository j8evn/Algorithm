def Per(loc):
    if loc==K:
        R.append(list(A))
        return
    for i in range(N):
        A[loc]= i+1
        Per(loc+1)

N, K= map(int,input().split())
A= [-1]*K
R= []
Per(0)
for i in range(len(R)):
    R[i]= map(str,R[i])
    print(' '.join(R[i]))