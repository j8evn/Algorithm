N= int(input())
A=[False]*100
G= list(map(int,input().split()))
rejected= 0
for i in range(N):
    if(A[G[i]-1]==False):
        A[G[i]-1]= True
    else:
        rejected= rejected+ 1
print(rejected)
