import sys
input= sys.stdin.readline

n= int(input())
A= []
for _ in range(n):
    A.append(list(input().split()))

Stack, R= [], [0]
i= 0
while A[i][0]!='DONE':
    if A[i][0]=='PUSH':
        Stack.append(int(A[i][1]))
        i += 1
    elif A[i][0]=='STORE':
        R.append(Stack.pop())
        i += 1
    elif A[i][0]=='LOAD':
        Stack.append(R[-1])
        i += 1
    elif A[i][0]=='PLUS':
        Stack.append(Stack.pop()+Stack.pop())
        i += 1
    elif A[i][0]=='TIMES':
        Stack.append(Stack.pop()*Stack.pop())
        i += 1
    elif A[i][0]=='IFZERO':
        if Stack.pop()==0:
            i= int(A[i][1])
        else:
            i += 1
print(Stack[-1])