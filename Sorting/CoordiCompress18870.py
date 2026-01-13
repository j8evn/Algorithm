import sys
input= sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
B= list(set(A))
B.sort()
dic= {}
R= []
for i in range(len(B)):
    dic[B[i]]= i
for i in range(N):
    R.append(dic[A[i]])
R= map(str,R)
print(' '.join(R))