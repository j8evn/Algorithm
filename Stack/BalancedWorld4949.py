import sys
input= sys.stdin.readline

R= []
while True:
    ss= input().rstrip()
    if ss=='.':
        break
    Stack= []
    for i in range(len(ss)):
        if ss[i]=='(' or ss[i]=='[':
            Stack.append(ss[i])
        elif ss[i]==']':
            if Stack and Stack[-1]=='[':
                Stack.pop()
            else:
                Stack.append(ss[i])
        elif ss[i]==')':
            if Stack and Stack[-1]=='(':
                Stack.pop()
            else:
                Stack.append(ss[i])
    if Stack:
        print("no")
    else:
        print("yes")