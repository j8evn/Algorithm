import sys
input= sys.stdin.readline

A= list(map(int,input().split()))
A.sort()
t= int(input())

R= set()
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        if A[i]+A[j]==t:
            R.add(str(A[i])+" "+str(A[j]))
R= list(R)
R.sort()
if R:
    print(*R, sep="\n")
print(len(R))