import sys
input= sys.stdin.readline

b, c, d= map(int,input().split())
B= list(map(int,input().split()))
C= list(map(int,input().split()))
D= list(map(int,input().split()))
B.sort(reverse=True)
C.sort(reverse=True)
D.sort(reverse=True)

r1, r2= 0, 0
for i in range(min(b,c,d)):
    r1 += (B[i]+C[i]+D[i])
    r2 += (B[i]+C[i]+D[i])*0.9
r1= r1+ sum(B[i+1:])+sum(C[i+1:])+sum(D[i+1:])
r2= r2+ sum(B[i+1:])+sum(C[i+1:])+sum(D[i+1:])
print(r1)
print(int(r2))