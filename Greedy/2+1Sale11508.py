import sys
input= sys.stdin.readline

N= int(input())
C= []
for _ in range(N):
    C.append(int(input()))
C.sort(reverse=True)

t= 0
for i in range(N):
    if (i+1)%3==0:
        continue
    t += C[i]
print(t)