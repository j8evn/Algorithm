N= int(input())
A= list(map(int,input().split()))
A.sort()
p, s= 0, 0
i, j= 0, N-1
while i<j:
    s += A[i]
    p += A[j]
    i, j= i+1, j-1
if N%2==0:
    print(s, p)
else:
    print(s, p+A[j])