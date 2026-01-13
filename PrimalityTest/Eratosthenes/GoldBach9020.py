import sys
input= sys.stdin.readline

def Goldbach(n):
    if n==4:
        R.append([2,2])
        return
    for i in range(3, n//2+1, 2):
        if ((P[i]==True) and (P[n-i]==True)):
            R.append([i,n-i])

P = [True]*10001
for i in range(2,10001): 
    if (P[i] == True):
        u = i*2
        while (u<=10000):
            P[u] = False
            u =u+i
T= int(input())
for _ in range(T):
    R= []
    n= int(input())
    Goldbach(n)
    print(R[-1][0], R[-1][1])