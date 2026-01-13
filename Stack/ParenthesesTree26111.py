s= input().strip()
cnt= 0
Stack= []
k= False
for i in range(len(s)):
    if s[i]=='(':
        Stack.append('(')
        k= True
    else:
        if Stack and k==True:
            cnt += (len(Stack)-1)
            Stack.pop()
            k= False
        elif Stack and k==False:
            Stack.pop()
print(cnt)