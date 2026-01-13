import sys
input= sys.stdin.readline

idx= 0
while True:
    idx += 1
    N= int(input())
    if N==0:
        break
    S= []
    for _ in range(N):
        S.append(input().rstrip())
    S.sort()
    print(idx)
    print("\n".join(S))
