N= int(input())
Stack, T, R= [], [], []
for i in range(N):
    T.append(int(input()))
idx= 0
for i in range(N):
    if len(Stack)==0 or T[i]!=Stack[-1]:
        for j in range(idx,T[i]):
            R.append("+")
            Stack.append(j+1)
        idx= T[i]
    if Stack and T[i]==Stack[-1]:
        R.append("-")
        Stack.pop()
if len(Stack)==0:
    print('\n'.join(R))
else:
    print("NO")
