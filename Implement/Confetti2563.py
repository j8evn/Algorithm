A=[]
for i in range(100):
    A.append([0]*100)
N=int(input())
for i in range(N):
    sr,sc=map(int,input().split())
    sr,sc=sr-1,sc-1
    for r in range(10):
        for c in range(10):
            A[sr+r][sc+c]=1
cnt=0
for r in range(100):
    for c in range(100):
        cnt+=A[r][c]
print(cnt)
