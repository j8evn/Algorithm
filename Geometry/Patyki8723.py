A= list(map(int,input().split()))
A.sort()
if A[0]==A[1]==A[2]:
    print(2)
elif A[0]**2+A[1]**2==A[2]**2:
    print(1)
else:
    print(0)