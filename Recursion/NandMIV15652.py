def Com(loc,f):
    if loc==K:
        R.append(list(A))
        return
    for i in range(f,N):
        A[loc]= i+1
        Com(loc+1,i)

N, K= map(int,input().split())
A= [-1]*K
R= []
Com(0,0)
for i in range(len(R)):
    R[i]= map(str,R[i])
    print(' '.join(R[i]))