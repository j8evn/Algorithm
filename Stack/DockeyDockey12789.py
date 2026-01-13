N= int(input())
A= list(map(int,input().split()))
A.reverse()
R, Stack= [], []

while A:
    if A[-1]==1:
        R.append(A.pop())
    else:
        if R and Stack and R[-1]+1==Stack[-1]:
            R.append(Stack.pop())
        elif R and R[-1]+1==A[-1]:
            R.append(A.pop())
        else:
            Stack.append(A.pop())

while Stack:
    if R and R[-1]+1==Stack[-1]:
        R.append(Stack.pop())
    else:
        break

if Stack:
    print("Sad")
else:
    print("Nice")
