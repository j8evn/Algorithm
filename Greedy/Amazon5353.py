import sys
input= sys.stdin.readline

while True:
    N= int(input())
    if N==0:
        break
    A= []
    for _ in range(N):
        A.append(list(map(int,input().split())))
    A.sort(key=lambda x:x[1])
    R= [A[0][1]]
    for i in range(1,N):
        if R[-1]<=A[i][0]:
            R.append(A[i][1])
    print(len(R))