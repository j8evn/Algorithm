n= int(input())
N= []
for _ in range(n):
    N.append(int(input()))
cnt= 0
Stack= []
for i in range(n):
    while Stack and Stack[-1]<=N[i]:
        Stack.pop()
    Stack.append(N[i])
#    print(Stack)
    cnt += len(Stack)-1
print(cnt)