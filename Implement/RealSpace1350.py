import math
import sys
input= sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
C= int(input())

cnt= 0
for i in range(N):
    cnt += math.ceil(A[i]/C)
print(cnt*C)