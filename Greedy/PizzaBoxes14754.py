M, N= map(int,input().split())
A=[]
for i in range(M):
    A.append(list(map(int,input().split())))
ss, tot= set([]), 0
for i in range(M):
    tot= tot+ sum(A[i])
    ss.add(max(A[i]))
for j in range(N):
    mm= -1
    for i in range(M):
        mm= max(mm,A[i][j])
    ss.add(mm)
ss= list(ss)
print(tot-sum(ss))
