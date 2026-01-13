import sys
input = sys.stdin.readline
T=int(input())
A=[]
for i in range(T):
    a,b=map(int,input().split())
    A.append(a+b)
A=list(map(str,A))
print('\n'.join(A))
