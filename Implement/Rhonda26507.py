import sys
input= sys.stdin.readline

n= int(input())
S= []
for _ in range(n):
    for i in range(10):
        S.append(list(map(int,input().strip())))
    input()
    
m= int(input())
for _ in range(m):
    tt= list(map(int,input().split()))
    R= [[0 for _ in range(10)] for _ in range(10)]
    for k in range(len(tt)):
        for i in range(10):
            for j in range(10):
                R[i][j] += S[tt[k]*10+i][j]
    
    for i in range(10):
        for j in range(10):
            if R[i][j]<10:
                R[i][j]= "0"+str(R[i][j])
            else:
                R[i][j]= str(R[i][j])
        print(*R[i])
    print()