import math

def MyCeil(a,b):
	tt= a//b
	if a%b!=0:
		tt += 1
	return tt

def CalcCost(m):
	if m<=0:
		return 10000000000
	return (m*X+K*P/m)

K, P, X= map(int,input().split())
m1= int(math.sqrt(K*P/X))
m2= m1-1
m3= m1+1

tt= CalcCost(m1)
tt= min(tt,CalcCost(m2))
tt= min(tt,CalcCost(m3))
print('%.3f'%tt)