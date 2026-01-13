from collections import deque

N, M= map(int,input().split())
ll= list(map(int,input().split()))
D= deque()
for i in range(N):
    D.append(i+1)
cnt= 0
for i in range(M):
    if D.index(ll[i]) <= len(D)-D.index(ll[i]):
        while D[0]!=ll[i]:
            D.rotate(-1)
            cnt += 1
        D.popleft()
    else:
        while D[0]!=ll[i]:
            D.rotate()
            cnt += 1
        D.popleft()
print(cnt)