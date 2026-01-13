import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
for b in B:
    if ((b in A)==True):
        print(1)
    else:
        print(0)
