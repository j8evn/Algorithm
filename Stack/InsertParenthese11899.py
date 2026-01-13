S= input().strip()
Stack= []
for i in range(len(S)):
    if Stack:
        if Stack[-1]=='(' and S[i]==')':
            Stack.pop()
        else:
            Stack.append(S[i])
    else:
        Stack.append(S[i])
print(len(Stack))