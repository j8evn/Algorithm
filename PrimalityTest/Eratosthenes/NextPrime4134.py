import sys
input= sys.stdin.readline

def IsPrime(n):
    if n==0 or n==1:
        return False
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

T= int(input())
for _ in range(T):
    n= int(input())
    while True:
        if IsPrime(n)==True:
            print(n)
            break
        n += 1
