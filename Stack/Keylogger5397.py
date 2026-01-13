L= int(input())
for i in range(L):
    Stack, shift= [], []
    ss= input().strip()
    for j in range(len(ss)):
        if ss[j]=='-':
            if Stack:
                Stack.pop()
        elif ss[j]=='<':
            if Stack:
                shift.append(Stack.pop())
        elif ss[j]=='>':
            if shift:
                Stack.append(shift.pop())
        else:
            Stack.append(ss[j])
    for j in range(len(shift)):
        Stack.append(shift[len(shift)-j-1])
    print(''.join(Stack))
