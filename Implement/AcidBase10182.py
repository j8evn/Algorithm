import math
import sys
input= sys.stdin.readline

n= int(input())
for _ in range(n):
    A= list(input().split())
    if A[0]=="H":
        print("{:.2f}".format(-math.log10(float(A[2]))))
    else:
        print("{:.2f}".format(14+math.log10(float(A[2]))))