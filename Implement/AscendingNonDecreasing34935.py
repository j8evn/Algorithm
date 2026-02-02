import sys
input= sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))

ascending= True
for i in range(N-1):
    if A[i] >= A[i+1]:
        ascending = False
        break

if ascending:
    print(1)
else:
    print(0)