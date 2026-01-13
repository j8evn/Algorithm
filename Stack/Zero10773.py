k= int(input())
stack= []
for i in range(k):
    s= int(input())
    if s==0:
        stack.pop()
    else:
        stack.append(s)
print(sum(stack))
