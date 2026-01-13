def Com(loc,f):
    if loc==K:
        R.append(list(A))
        return
    for i in range(f,N):
        A[loc]= i
        Com(loc+1,i+1)

N, K= map(int,input().split())
P= list(map(int,input().split()))
A= [-1]*K
R= []
Com(0,0)

for i in range(len(R)):
    for j in range(len(R[i])):
        R[i][j]= P[R[i][j]]
    R[i].sort()
for i in range(len(R[0])-1,-1,-1):
    R.sort(key=lambda x:x[i])
for i in range(len(R)):
    R[i]= map(str,R[i])
    print(' '.join(R[i]))