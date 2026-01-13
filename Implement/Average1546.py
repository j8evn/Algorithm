N=int(input())
A=list(map(int,input().split()))
mm=max(A)
for i in range(N):
    A[i]=A[i]*100/mm
av=sum(A)/N
print(av)
