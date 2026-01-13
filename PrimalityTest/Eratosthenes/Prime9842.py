def IsPrime(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

n= int(input())
cnt, N= 0, 2
while cnt!=n:
    if IsPrime(N):
        cnt += 1
    N += 1
print(N-1)