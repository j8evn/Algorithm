T= int(input())
C= int(input())
A= []
for _ in range(C):
    A.append(int(input()))
A.sort()

cnt= 0
for i in range(C):
    if T-A[i]<0:
        break
    T= T-A[i]
    cnt += 1
print(cnt)