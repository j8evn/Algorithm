ss= input().strip()
Stack= []
for i in range(len(ss)):
    if ss[i]=='(':
        Stack.append(ss[i])
    elif ss[i]==')':
        temp= 0
        while True:
            t= Stack.pop()
            if t=="(":
                break
            temp += t
        Stack.append(temp)
    elif ss[i]=='H':
        Stack.append(1)
    elif ss[i]=='C':
        Stack.append(12)
    elif ss[i]=='O':
        Stack.append(16)
    else:
        Stack.append(Stack.pop()*int(ss[i]))
print(sum(Stack))