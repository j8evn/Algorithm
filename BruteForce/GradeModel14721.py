def f(x,a,b):
    return a*x+b
    
def RSS(a,b):
    s= 0
    for i in range(n):
        s += (A[i][1]-f(A[i][0],a,b))**2
    return s

n= int(input())
A= []
for i in range(n):
    A.append(list(map(int,input().split())))

mm, ma, mb= RSS(1,1), 1, 1
for a in range(1,101):
    for b in range(1,101):
        if RSS(a,b)<mm:
            mm, ma, mb= RSS(a,b), a, b
print(ma,mb)
