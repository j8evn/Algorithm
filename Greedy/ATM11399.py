import sys
input=sys.stdin.readline

P=[]
hap=0
N=int(input())
P=list(map(int,input().split()))
P.sort()
for i in range(N):
    for j in range(i+1):
        hap+=P[j]
print(hap)
