import math
import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    m, n= map(int,input().split())
    print(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))