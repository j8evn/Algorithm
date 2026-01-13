import math

mn, mx= map(int,input().split())
A= [True]*(mx-mn+1)

for i in range(2,int(math.sqrt(mx))+1):
    s= ((mn+(i*i)-1)//(i*i))*(i*i)
    for j in range(s,mx+1,i*i):
        A[j-mn]= False

cnt= 0
for i in range(len(A)):
    if A[i]==True:
        cnt += 1
print(cnt)
