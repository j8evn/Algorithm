import sys
input=sys.stdin.readline

N=int(input())
n=list(map(int,input().split()))
cnt=1
for i in range(N-1):
    if (n[i]+n[i+1])%2!=0:
        cnt+=1
print(cnt)
