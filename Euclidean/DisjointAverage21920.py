import math

n= int(input())
A= list(map(int,input().split()))
x= int(input())

R= []
for i in range(n):
	if math.gcd(x,A[i])==1:
		R.append(A[i])
print(sum(R)/len(R))