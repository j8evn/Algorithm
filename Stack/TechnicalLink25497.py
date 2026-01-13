N= int(input())
T= input().strip()
Stack1, Stack2= [], []
cnt= 0
for i in range(N):
    if T[i]=='S':
        Stack1.append(T[i])
    elif T[i]=='K':
        if Stack1 and Stack1[-1]=='S':
            Stack1.pop()
            cnt += 1
        else:
            break
    elif T[i]=='L':
        Stack2.append(T[i])
    elif T[i]=='R':
        if Stack2 and Stack2[-1]=='L':
            Stack2.pop()
            cnt += 1
        else:
            break
    else:
        cnt += 1
print(cnt)