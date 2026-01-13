T= int(input())
for i in range(T):
    n= int(input())
    A=(list(map(int,input().split())))
    A.sort(reverse=True)
    B=[-1]*n
    l, r= 0, n-1
    for j in range(n):
        if(j%2==0):
            B[l]=(A[j])
            l+= 1
        else:
            B[r]=(A[j])
            r-= 1
    mm= -1
    for j in range(n-1):
        mm= max(abs(B[j]-B[j+1]),mm)
    print(mm)
