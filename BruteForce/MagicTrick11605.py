import sys
input= sys.stdin.readline

n= int(input())
cnt= 0
A= []
for i in range(n):
    A.append(list(input().split()))
    A[i][1]= int(A[i][1])
for i in range(1,101):
    c= i
    for j in range(n):
        if A[j][0]=='ADD':
            c= c+A[j][1]
        elif A[j][0]=='MULTIPLY':
            c= c*A[j][1]
        elif A[j][0]=='SUBTRACT':
            c= c-A[j][1]
            if c<0:
                cnt += 1
                break
        elif A[j][0]=='DIVIDE':
            if c/A[j][1] != c//A[j][1]:
                cnt += 1
                break
            c= c/A[j][1]
print(cnt)