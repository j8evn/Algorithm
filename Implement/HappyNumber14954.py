def ff(n):
    ss= 0
    while(n>0):
        t= n%10
        n= n//10
        ss= ss+ t*t
    return ss

n= int(input())
s= set([])
s.add(n)
while(True):
    n= ff(n)
    if(n==1):
        print("HAPPY")
        break
    if((n in s)==True):
        print("UNHAPPY")
        break
    s.add(n)
