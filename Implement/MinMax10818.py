N=int(input())
A=list(map(int,input().split()))
m=-1000001
M=1000001

for i in range(N):
    if (M>A[i]):
        M=A[i]
print(M, end=' ')
for i in range(N):
    if (m<A[i]):
        m=A[i]
print(m)
