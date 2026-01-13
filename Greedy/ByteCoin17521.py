n, w= map(int,input().split())
A=[100000]
for i in range(n):
    t= int(input())
    if (t != A[-1]):
        A.append(t)

n= len(A)
cur= 0
for i in range(1,n-1):
    if((A[i]>A[i-1]) and (A[i]>A[i+1])):
        w= w+ A[i]*cur
        cur= 0
    elif((A[i]<A[i-1]) and (A[i]<A[i+1])):
        cur= w//A[i]
        w= w%A[i]
w= w+ cur*A[-1]
print(w)
