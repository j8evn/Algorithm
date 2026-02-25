N= int(input())
A= list(map(int,input().split()))
ll= [0, 1, 2]

cnt= 0
j= 0
for i in range(N):
    if j==3:
        j= 0
    if A[i]==ll[j]:
        cnt += 1
        j += 1
    
print(cnt)