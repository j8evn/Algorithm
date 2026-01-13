def GoodWord(s):
    Stack= []
    for i in range(len(s)):
        if len(Stack)==0:
            Stack.append(s[i])
        elif Stack[-1]!=s[i]:
            Stack.append(s[i])
        else:
            Stack.pop()
    if Stack:
        return 0
    else:
        return 1

n= int(input())
cnt= 0
for i in range(n):
    s= input().strip()
    cnt += GoodWord(s)
print(cnt)
