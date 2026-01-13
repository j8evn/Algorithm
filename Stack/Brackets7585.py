import sys
input= sys.stdin.readline

while True:
    Stack= []
    ss= input().rstrip()
    if ss=="#":
        break
    for i in range(len(ss)):
        if ss[i]=='(' or ss[i]=='{' or ss[i]=='[':
            Stack.append(ss[i])
        elif ss[i]==')':
            if Stack and Stack[-1]=='(':
                Stack.pop()
            else:
                Stack.append(ss[i])
        elif ss[i]=='}':
            if Stack and Stack[-1]=='{':
                Stack.pop()
            else:
                Stack.append(ss[i])
        elif ss[i]==']':
            if Stack and Stack[-1]=='[':
                Stack.pop()
            else:
                Stack.append(ss[i])
    if Stack:
        print("Illegal")
    else:
        print("Legal")