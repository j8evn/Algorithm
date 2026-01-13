N, M= map(int,input().split())
cnt= 0
for _ in range(N):
    S= list(input().strip())
    o= S.count('O')
    if len(S)-o<o:
        cnt += 1
print(cnt)