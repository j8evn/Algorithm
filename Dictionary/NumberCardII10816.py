import sys
input= sys.stdin.readline

n= int(input())
N= list(map(int,input().split()))
m= int(input())
M= list(map(int,input().split()))
D= {}

for i in N:
    if i in D:
        D[i] += 1
    else:
        D[i]= 1

R= []
for j in M:
    if j in D:
        R.append(D[j])
    else:
        R.append(0)
R= map(str,R)
print(' '.join(R))