'''
N=int(input())
A=list(input().strip())
A=map(int,A)
print(sum(A))
'''

N=int(input())
N=int(input())
ss=0
while (N!=0):
    ss=ss+N%10
    N=N//10
print(ss)
