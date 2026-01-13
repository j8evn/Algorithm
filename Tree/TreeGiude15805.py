N= int(input())
A= list(map(int,input().split()))
K= [-2]*(max(A)+1)
K[A[0]]= -1
for i in range(1,N):
    if K[A[i]]==-2:
        K[A[i]]= A[i-1]
print(len(K))
K= map(str,K)
print(' '.join(K))