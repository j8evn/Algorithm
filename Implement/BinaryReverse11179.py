def Binary(n):
    r= []
    while (n>0):
        r.append(n%2)
        n= n//2
    return r

n= int(input())
new= Binary(n)
new.reverse()
a= 0
for i in range(len(new)):
    if new[i]==1:
        a += 2**(i)
print(a)
