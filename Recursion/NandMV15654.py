def Per(loc):
    if loc==K:
        R.append(list(A))
        return
    for i in range(N):
        if V[i]==False:
            V[i]= True
            A[loc]= i
            Per(loc+1)
            V[i]= False

N, K= map(int,input().split())
P= list(map(int,input().split()))
A= [-1]*K
V= [False]*N
R= []
Per(0)
for i in range(len(R)):
    for j in range(len(R[i])):
        R[i][j]= P[R[i][j]]
for i in range(len(R[0])-1,-1,-1):
    R.sort(key=lambda x:x[i])
for i in range(len(R)):
    R[i]= map(str,R[i])
    print(' '.join(R[i]))