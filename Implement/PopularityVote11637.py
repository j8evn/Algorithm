import sys
input= sys.stdin.readline

t= int(input())
for i in range(t):
    n= int(input())
    A= []
    for j in range(n):
        A.append(int(input()))
    cnt, idx= 0, 0
    for j in range(n):
        if max(A)==A[j]:
            cnt += 1
            idx= j
    if cnt==1:
        if max(A)>sum(A)-max(A):
            print("majority winner "+ str(idx+1))
        else:
            print("minority winner "+ str(idx+1))
    else:
        print("no winner")
