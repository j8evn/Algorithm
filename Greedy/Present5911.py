import sys
input= sys.stdin.readline

N, B= map(int,input().split())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))
A.sort(key= lambda x: x[0]+x[1])

mm= 0
for i in range(N):
    s= A[i][0]//2+ A[i][1]
    if s > B:
        continue
    cnt= 1
    for j in range(N):
        if i==j:
            continue
        if B >= s+A[j][0]+A[j][1]:
            s += A[j][0]+A[j][1]
            cnt += 1
        else:
            break
    mm= max(mm, cnt)
print(mm)