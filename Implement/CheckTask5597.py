A=[False]*30
for i in range(28):
    n=int(input())
    A[n-1]=True
for i in range(30):
    if (A[i]==False):
        print(i+1)
