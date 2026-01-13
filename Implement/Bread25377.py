N = int(input())
ans = 1010
for i in range(N):
    A, B = map(int, input().split())
    if A<=B:
        ans = min(ans, B)
if ans==1010:
    print("-1")
else:
    print(ans)
