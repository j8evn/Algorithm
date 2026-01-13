import sys
input= sys.stdin.readline

n= int(input())
Stack= []
for i in range(n):
    k= list(map(int,input().split()))
    if k[0]==1:
        Stack.append(k[1])
    elif k[0]==2:
        if len(Stack)==0:
            print(-1)
        else:
            print(Stack.pop())
    elif k[0]==3:
        print(len(Stack))
    elif k[0]==4:
        if len(Stack)==0:
            print(1)
        else:
            print(0)
    elif k[0]==5:
        if len(Stack)==0:
            print(-1)
        else:
            print(Stack[-1])