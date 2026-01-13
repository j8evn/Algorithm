hap=0
A=[]
M=int(input())
N=int(input())
for i in range(M,N+1):
    for j in range(i+1):
        if (j**2==i):
            A.append(i)
            hap+=i
if A==[]:
    print(-1)
else:
    print(hap)
    print(min(A))
