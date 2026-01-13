N= int(input())
A= list(map(int,input().split()))
R= [0]*N
if A[0]==0:
    R[0]= -1
else:
    R[0]= 1
for i in range(1,N):
    if A[i]==0:
        R[i]= R[i-1]-1
    else:
        R[i]= R[i-1]+1
print(sum(R))