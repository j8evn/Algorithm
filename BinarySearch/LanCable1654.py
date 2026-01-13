import sys
input= sys.stdin.readline

def Bin(low,high):
    if low > high:
        return
    global r
    mid= (low+high)//2
    cnt= 0
    for i in range(k):
        cnt += K[i]//mid
    if cnt >= N:
        r= mid
        Bin(mid+1,high)
    else:
        Bin(low,mid-1)

k, N= map(int,input().split())
K= []
for _ in range(k):
    K.append(int(input()))
s= max(K)
r= 0
Bin(0,s*2)
print(r)