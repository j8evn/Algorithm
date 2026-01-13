import sys
input=sys.stdin.readline

N,k=map(int,input().split())
n=list(map(int,input().split()))
n.sort(reverse=True)
print(n[k-1])
