N, K= map(int,input().split())
A= list(map(int,input().split()))
A.sort()
A.insert(0,0)
R= []
for i in range(N):
    R.append(A[i+1]-A[i])
R.sort()
for _ in range(K):
    R.pop()
print(sum(R))