import sys
input= sys.stdin.readline

N, T= map(int,input().split())
Stack= []
for _ in range(N):
    w, v= map(int,input().split())
    cal= w+v*T
    if not Stack:
        Stack.append(cal)
    else:
        if Stack[-1]>=cal:
            while Stack and Stack[-1]>=cal:
                Stack.pop()
            Stack.append(cal)
        else:
            Stack.append(cal)
print(len(Stack))