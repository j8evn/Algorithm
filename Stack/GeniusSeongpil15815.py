exp= input()
Stack= []
for i in range(len(exp)):
    if ord(exp[i])>=ord('0') and ord(exp[i])<=ord('9'):
        Stack.append(int(exp[i]))
    else:
        t2= Stack.pop()
        t1= Stack.pop()
        if exp[i]=='+':
            Stack.append(t1+t2)
        elif exp[i]=='-':
            Stack.append(t1-t2)
        elif exp[i]=='*':
            Stack.append(t1*t2)
        elif exp[i]=='/':
            Stack.append(t1//t2)
print(Stack.pop())
