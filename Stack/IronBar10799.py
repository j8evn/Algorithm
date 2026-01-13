s= input().strip()
Stack= []
cnt= 0
for i in range(len(s)):
    if s[i]=='(':
        Stack.append(s[i])
    else:
        if s[i-1]=='(':
            Stack.pop()
            cnt += len(Stack)
        else:
            cnt += 1
            Stack.pop()
print(cnt)