import copy

r, c= map(int,input().split())
A= []
for i in range(r):
    A.append(list(input()))
a, b= map(int,input().split())

for i in range(r):
    for j in range(c):
        A[i].append(copy.deepcopy(A[i][c-j-1]))
for i in range(r):
    A.append(copy.deepcopy(A[r-i-1]))

if A[a-1][b-1]=='#':
    A[a-1][b-1]= '.'
elif A[a-1][b-1]=='.':
    A[a-1][b-1]= '#'

for i in range(r*2):
    print(''.join(A[i]))
