n= int(input())
N= list(map(int,input().split()))
G= []
Stack= []
for i in range(n):
    while Stack:
        if (Stack[-1][0]<N[i]):
            Stack.pop()
        else:
            G.append(Stack[-1][1]+1)
            Stack.append([N[i],i])
            break
    if (len(Stack)==0):
        G.append(0)
        Stack.append([N[i],i])
print(*G)