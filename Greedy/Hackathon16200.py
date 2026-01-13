N= int(input())
X= list(map(int,input().split()))
X.sort()

cnt= 0
t, c= 0, 0
for i in range(N):
    if c==0:
        t= X[i]
    c += 1
    if c==t:
        c= 0
        cnt += 1
if c!=0:
    cnt += 1

print(cnt)