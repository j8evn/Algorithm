import sys
input= sys.stdin.readline

def Goldbach(n):
    for i in range(3, n, 2):
        if ((P[i]==True) and (P[n-i]==True)):
            return str(n)+" = "+str(i)+" + "+str(n-i)
    return "Goldbach's conjecture is wrong."

# 에라토스테네스의 채 (소수 찾기)
P = [True]*1000001 # n의 가능한 범위 1000000까지 
for i in range(2,1000001): 
    if (P[i] == True):
        u = i*2
        while (u<=1000000):
            P[u] = False
            u =u+i
R= []
while True:
    n= int(input())
    if n==0:
        break
    R.append(Goldbach(n))
print("\n".join(R))
