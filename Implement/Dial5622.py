import sys
input=sys.stdin.readline

N=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

a=list(input().strip())
result=0
for i in range(len(a)):
    for j in range(len(N)):
        if a[i] in N[j]:
            result+=N.index(N[j])+3
print(result)
