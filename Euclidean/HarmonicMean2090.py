import sys
input=sys.stdin.readline

def gcd(m,n): 
	if (n>m):
		m, n = n,m 
	if (n==0):
		return m
	while m!=0: 
		m = m % n 
		if (m==0): 
			return n 
		m,n = n,m
		
N=int(input())
A=list(map(int,input().split()))
ss = 1
for i in range(N):
	ss = ss*A[i]
n1 =0
for i in range(N):
	n1 += ss//A[i]
g = gcd(n1, ss)
print(str(ss//g)+"/"+str(n1//g))
