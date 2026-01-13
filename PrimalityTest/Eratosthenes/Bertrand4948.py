import sys
input=sys.stdin.readline

def IsPrime(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

while True:
    n=int(input())
    N=2*n
    if (n==0):
        break
    cnt=0
    for i in range(n+1,N+1):
        if (IsPrime(i)==True):
            cnt+=1
    print(cnt)