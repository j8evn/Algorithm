import sys
input= sys.stdin.readline

bar= input().rstrip()
N= int(input())
cnt= 1
S= set([bar])

for _ in range(N):
    z1, z2= input().split()
    if z2==bar:
        bar= z1
        if z1 in S:
            continue
        S.add(z1)
        cnt += 1

print(bar)
print(cnt)