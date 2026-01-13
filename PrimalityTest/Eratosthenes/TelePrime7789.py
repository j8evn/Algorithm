def IsPrime(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

o, n= input().split()
if IsPrime(int(o)) and IsPrime(int(n+o)):
    print("Yes")
else:
    print("No")