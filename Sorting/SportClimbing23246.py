n= int(input())
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
A.sort(key=lambda x:x[0])
A.sort(key=lambda x:x[1]+x[2]+x[3])
A.sort(key=lambda x:x[1]*x[2]*x[3])
print(A[0][0],A[1][0],A[2][0])
