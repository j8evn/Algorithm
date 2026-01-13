N= int(input())
S= set()
for _ in range(N):
    ss= list(input().strip())
    ss.sort()
    S.add(str(ss))
print(len(S))