import sys
input= sys.stdin.readline

n= int(input())
b= list(map(int,input().split()))
p= list(map(int,input().split()))
b1= max(b)
if b.count(b1)==1:
    b2= -1
    for i in range(n):
        if b[i] != b1:
            b2= max(b2,b[i])
else:
    b2= b1

R= []
for i in range(n):
    if b[i]==b1:
        c= b2- p[i]
    else:
        c= b1- p[i]
    R.append(b[i]-c-p[i])

R= map(str,R)
print(' '.join(R))
