import sys
input= sys.stdin.readline

while True:
    n= int(input())
    if n==0:
        break
    t= 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            t += i*j
    print(t)