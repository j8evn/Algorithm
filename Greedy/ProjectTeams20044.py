n= int(input())
A= list(map(int,input().split()))
A.sort()
mm= 1000000
for i in range(n):
    mm= min((A[i]+A[-1-i]),mm)
print(mm)
