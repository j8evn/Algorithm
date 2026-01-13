import copy
import sys
input= sys.stdin.readline

n= int(input())
A= list(map(int,input().split()))
A.sort()

s= sum(A)-A[0]
R= 0
for i in range(n-1):
    R += A[i]*s
    s= s-A[i+1]
print(R)