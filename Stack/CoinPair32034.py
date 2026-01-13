import sys
input= sys.stdin.readline

T= int(input())
for i in range(T):
    N= int(input())
    S= input().strip()
    cnt= 0
    Stack= []
    for j in range(len(S)):
        if S[j]=='T' and len(Stack)==0:
            Stack.append(j)
        elif S[j]=='T' and (j-Stack[-1]-1)%2==1:
            Stack.append(j)
        elif S[j]=='T' and (j-Stack[-1]-1)%2==0:
            cnt += ((j-Stack[-1]-1) + 1)
            Stack.pop()
            
    if len(Stack)==0:
        print(cnt)
    else:
        print(-1)
