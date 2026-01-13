import sys
input= sys.stdin.readline

ss= list(input().strip())
Stack= []
M= int(input())
for _ in range(M):
    m= list(input().split())
    if m[0]=='P':
        ss.append(m[1])
    elif m[0]=='L' and ss:
        Stack.append(ss.pop())
    elif m[0]=='D' and Stack:
        ss.append(Stack.pop())
    elif m[0]=='B' and ss:
        ss.pop()
while Stack:
    ss.append(Stack.pop())
print(*ss, sep='')