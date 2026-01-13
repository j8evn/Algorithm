from collections import deque
import sys
input= sys.stdin.readline

N= int(input())
if N==0:
    print(0)
else:
    A= []
    for _ in range(N):
        A.append(int(input()))
    A.sort()
    A= deque(A)

    k= N*(15/100)
    if (N*(15/100)-int(k))*10 >= 5:
        k= int(k)+1
    else:
        k= int(k)

    for i in range(k):
        A.pop()
        A.popleft()
    avg= sum(A)/len(A)
    if (avg-int(avg))*10 >= 5:
        avg= int(avg)+1
    else:
        avg= int(avg)
    print(avg)