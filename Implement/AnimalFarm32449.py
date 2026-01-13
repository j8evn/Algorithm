import sys
input= sys.stdin.readline

n= int(input())
other= []
pig= 0
for _ in range(n):
    s, a= input().split()
    a= int(a)
    if s=='pig':
        pig= max(pig,a)
    else:
        other.append(a)

cnt= pig
for i in range(len(other)):
    if other[i]<pig:
        cnt += other[i]
print(cnt)