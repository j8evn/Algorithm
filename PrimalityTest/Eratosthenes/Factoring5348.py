import sys
input= sys.stdin.readline

def IsPrime(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

n= int(input())
for _ in range(n):
    t= int(input())
    if IsPrime(t)==True:
        print("{:d}: prime".format(t))
    else:
        tt= t   
        i= 2
        arr= []
        while(tt>1):
            if tt%i==0:
                arr.append(i)
                tt= tt//i
            else:
                i += 1
        print(str(t)+":", *arr)