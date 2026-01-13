import sys
input= sys.stdin.readline

N, M= map(int,input().split())
S= set()
for _ in range(N):
    S.add(input().strip())
cnt= 0
for _ in range(M):
    ss= input().strip()
    if ss in S:
        cnt += 1
print(cnt)