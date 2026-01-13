N= int(input())
A= list(map(int,input().split()))
B= A.copy()
B.insert(0,0)
for i in range(N):
    B[i+1] += B[i]
s= 0
for i in range(1,N+1):
    s += A[i-1]*(B[N]-B[i])
print(s%1000000007)