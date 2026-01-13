N= int(input())
Stack= []
for _ in range(N):
    n= int(input())
    if Stack:
        if Stack[-1]>n:
            Stack.append(n)
        else:
            while Stack and Stack[-1]<=n:
                Stack.pop()
            Stack.append(n)
    else:
        Stack.append(n)
print(len(Stack))