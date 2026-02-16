from math import factorial

t= int(input())
for _ in range(t):
    n= int(input())
    f= str(factorial(n))
    for i in range(len(f)-1, -1, -1):
        if f[i] != '0':
            print(f[i])
            break