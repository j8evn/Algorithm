n, b, a= map(int,input().split())
N= list(map(int,input().split()))
N.sort()
Stack, cur, cnt= [], 0, 0
for i in range(n):
    if cur+N[i] <= b:
        cur += N[i]
        cnt += 1
        Stack.append(N[i])
    else:
        Stack.append(N[i])
        cur += N[i]
        while len(Stack)>0 and a>0:
            e= Stack.pop()
            a -= 1
            if cur-e//2 <= b:
                cnt += 1
                cur -= e//2
                break
            else:
                cur -= e//2
print(cnt)