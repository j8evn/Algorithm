import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))
A.sort(key=lambda x:-x[2])

i, R= 1, []
if A[i-1][0]==A[i][0]:
    R.append([A[i-1][0],A[i-1][1]])
    R.append([A[i][0],A[i][1]])
    while R[1][0]==A[i][0]:
        i += 1
    R.append([A[i][0],A[i][1]])
else:
    R.append([A[0][0],A[0][1]])
    R.append([A[1][0],A[1][1]])
    R.append([A[2][0],A[2][1]])
for i in range(3):
    R[i]= map(str,R[i])
    print(' '.join(R[i]))