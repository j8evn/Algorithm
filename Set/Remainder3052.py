'''
A=[False]*42
for i in range(10):
    t=int(input())%42
    A[t]=True
cnt=0
for i in range(42):
    if(A[i]==True):
        cnt+=1
print(cnt)
'''

A=set()
for i in range(10):
    A.add(int(input())%42)
print(len(A))
