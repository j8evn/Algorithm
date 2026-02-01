import sys
input= sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
if A== sorted(A):
    print(1)
else:
    print(0)