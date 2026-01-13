icp = {'+':1, '-':1, '*':2, '/':2, '(':3}
isp = {'+':1, '-':1, '*':2, '/':2, '(':0}
ss= input().strip()
Stack, A= [], []
for i in range(len(ss)):
    if ord(ss[i])>=ord('A') and ord(ss[i])<=ord('Z'):
        A.append(ss[i])
    elif ss[i]==')':
        while Stack and Stack[-1]!='(':
            A.append(Stack.pop())
        Stack.pop()
    else: # ( + - * /
        while Stack and isp[Stack[-1]]>=icp[ss[i]]:
            A.append(Stack.pop())
        Stack.append(ss[i])
while Stack: # 스택이 비어있지 않을 때
    A.append(Stack.pop())
print(''.join(A))