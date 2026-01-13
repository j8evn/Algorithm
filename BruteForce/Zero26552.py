import sys
input= sys.stdin.readline

n= int(input())
for _ in range(n):
    k= int(input())
    k += 1
    while True:
        if '0' in str(k):
            k += 1
            continue
        print(k)
        break