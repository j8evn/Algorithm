N= int(input())
for i in range(N):
    A= []
    Stack= list(input().split())
    while Stack:
        A.append(Stack.pop())
    print("Case #{:d}: {}".format(i+1, ' '.join(A)))