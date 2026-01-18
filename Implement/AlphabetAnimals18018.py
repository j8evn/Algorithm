import sys
input= sys.stdin.readline

s= input().strip()
n= int(input())
A= [[] for _ in range(26)]

for _ in range(n):
    a= input().strip()
    A[ord(a[0])-ord('a')].append(a)

idx= ord(s[-1])-ord('a')

if not A[idx]:
    print("?")
else:
    win= None
    for w in A[idx]:
        end_idx= ord(w[-1])-ord('a')
        if not A[end_idx] or (end_idx==idx and len(A[end_idx])==1):
            win= w
            break

    if win:
        print(win+"!")
    else:
        print(A[idx][0])
