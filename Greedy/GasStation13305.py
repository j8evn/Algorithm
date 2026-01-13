import sys
input= sys.stdin.readline

N= int(input())
d= list(map(int,input().split()))
m= list(map(int,input().split()))

s= 0
mm= 1000000000
for i in range(N):
    if i==N-1:
        break
    mm= min(mm,m[i])
    s += d[i]*mm
print(s)