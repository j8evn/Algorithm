N=int(input())
A=[]
for i in range(N):
    a,b=map(int,input().split())
    s=b%a
    A.append(s)
print(sum(A))
