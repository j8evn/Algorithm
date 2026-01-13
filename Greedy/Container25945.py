import sys
input= sys.stdin.readline

n= int(input())
A= list(map(int,input().split()))
A.sort(reverse=True)
B= [(sum(A)//n)]*n
for i in range(sum(A)%n):
    B[i] += 1

cnt= 0
for i in range(n):
    t= A[i]-B[i]
    if t<0:
        break
    cnt += t
print(cnt)