m= int(input())
mx, mn, sx, sn= -1, 1000000000, -1, 1000000000
for _ in range(m):
    A= list(map(int,input().split()))
    mx, mn= max(mx,max(A[1:])), min(mn,min(A[1:]))
    sx, sn= max(sx,sum(A[1:])), min(sn,sum(A[1:]))
print(mx)
print(mn)
print(sx)
print(sn)