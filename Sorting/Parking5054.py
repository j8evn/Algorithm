import sys
input= sys.stdin.readline

t= int(input())
for i in range(t):
    n= int(input())
    xi= list(map(int,input().split()))
    xi.sort()
    print((xi[-1]-xi[0])*2)
