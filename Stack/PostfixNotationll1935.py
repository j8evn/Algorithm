n= int(input())
exp= input()
Stack, N= [], []
for i in range(n):
    N.append(int(input()))

for i in range(len(exp)):
    if ord(exp[i])>=ord('A') and ord(exp[i])<=ord('Z'):
        Stack.append(N[ord(exp[i])- ord('A')])
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
            Stack.append(t1/t2)
print('{:.2f}'.format(Stack.pop()))
