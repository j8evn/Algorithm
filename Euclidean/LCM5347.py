import math
import sys
input= sys.stdin.readline

n= int(input())
for _ in range(n):
	a, b= map(int,input().split())
	g= math.gcd(a,b)
	print(math.lcm(a,b))