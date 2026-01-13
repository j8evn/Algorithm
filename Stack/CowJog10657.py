import sys
input= sys.stdin.readline

N= int(input())
Stack= []
for _ in range(N):
    w, v= map(int,input().split())
    if not Stack:
        Stack.append(v)
    else:
        if Stack[-1]>v:
            while Stack and Stack[-1]>v:
                Stack.pop()
            Stack.append(v)
        else:
            Stack.append(v)
print(len(Stack))