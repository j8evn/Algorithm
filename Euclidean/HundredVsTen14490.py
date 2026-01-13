import math

n, m= map(int,input().split(':'))
g= math.gcd(n,m)
n= n//g
m= m//g

print("{:d}:{:d}".format(n,m))