import sys
input= sys.stdin.readline

Val, Lev, Seq, Left, Right= 0, 1, 2, 3, 4
N= int(input())
A= []
for i in range(N):
    v, lv= map(int,input().split())
    A.append([v,lv,i,-1,-1])
A.sort(key=lambda x:x[Val])

def Answer():
    rr= -1
    for i in range(N):
        if (A[i][Lev]==1):
            rr= i
            break
    if rr==-1:
        print(-1)
        return
    que, fr, cnt= [], 0, 0
    que.append(rr)
    while (len(que)!=fr):
        cnt += 1
        if (A[que[fr]][Left]!=-1):
            que.append(A[que[fr]][Left])
        if (A[que[fr]][Right]!=-1):
            que.append(A[que[fr]][Right])
        fr += 1
    if (cnt!=N):
        print(-1)
        return
    for i in range(N):
        if (A[i][Left]!=-1):
            A[i][Left]= A[A[i][Left]][Seq]+1
        if (A[i][Right]!=-1):
            A[i][Right]= A[A[i][Right]][Seq]+1
    A.sort(key=lambda x:x[Seq])
    R= []
    for i in range(N):
        R.append(str(A[i][Left])+" "+str(A[i][Right]))
    print("\n".join(R))

Stack= []
for i in range(N):
    if (len(Stack)==0):
        Stack.append(i)
        continue
    while ((len(Stack)>0) and (A[Stack[-1]][Lev] > A[i][Lev]+1)):
        Stack.pop()
    if len(Stack)>0:
        if (A[i][Lev]==A[Stack[-1]][Lev]-1):
            A[i][Left]= Stack[-1]
            Stack.pop()
        if (len(Stack)>0) and (A[i][Lev]==A[Stack[-1]][Lev]+1):
            A[Stack[-1]][Right]= i
        Stack.append(i)

Answer()