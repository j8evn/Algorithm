import sys
input= sys.stdin.readline

def Eval(x):
    return -x[1]*1000000000000 -x[2]*1000000 -x[3]

n, k= map(int,input().split())
A= []
for i in range(n):
    A.append(list(map(int,input().split())))
    
A.sort(key=Eval)
for i in range(n):
    if A[i][0]==k:
        break
while(i-1>=0 and Eval(A[i])==Eval(A[i-1])):
    i = i-1
print(i+1)
