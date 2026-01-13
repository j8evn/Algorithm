import sys
input= sys.stdin.readline

def vps(s):
    Stack= []
    for i in range(len(s)):
        if len(Stack)==0:
            Stack.append(s[i])
        elif Stack[-1]==s[i]:
            Stack.append(s[i])
        else:
            if Stack[-1]==')':
                Stack.append(s[i])
            else:
                Stack.pop()
    if len(Stack)==0:
        return "YES"
    else:
        return "NO"

n= int(input())
for i in range(n):
    s= input().strip()
    print(vps(s))
