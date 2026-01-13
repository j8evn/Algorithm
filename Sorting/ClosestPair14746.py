import sys
input= sys.stdin.readline
n, m= map(int,input().split())
c1, c2= map(int,input().split())
P= list(map(int,input().split()))
Q= list(map(int,input().split()))
P.sort()
Q.sort()
idx, mm, cnt= 0, 100000000, 0
for i in range(n):
    while(idx<m):
        tt= abs(P[i]-Q[idx])
        if(tt<mm):
            mm, cnt= tt, 1
        elif(tt==mm):
            cnt+= 1
        if(Q[idx]>P[i]):
            break
        idx+= 1
print(mm+abs(c2-c1), cnt)
