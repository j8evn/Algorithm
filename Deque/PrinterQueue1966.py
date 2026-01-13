from collections import deque
import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    dq= deque()
    N, M= map(int,input().split())
    A= list(map(int,input().split()))
    S= sorted(A, reverse=True)
    for i in range(N):
        dq.append([A[i],i])

    i, cnt= 0, 0
    while dq:
        if dq[0][0]!=S[i]:
            dq.append(dq.popleft())
        elif dq[0][0]==S[i]:
            if dq[0][1]==M:
                dq.popleft()
                cnt += 1
                print(cnt)
                break
            else:
                dq.popleft()
                cnt += 1
                i += 1