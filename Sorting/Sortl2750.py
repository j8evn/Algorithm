N=int(input())
A=[]
for i in range(N):
    n=int(input())
    A.append(n)
A.sort()
for i in range(N):
    print(A[i])
