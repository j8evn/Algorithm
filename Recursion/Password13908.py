def perm(n):
    if (n==K):
        Eval()
        return
    for i in range(10):
        A[n]= i
        perm(n+1)

def Eval():
    global cnt
    t= list(map(str,A))
    for i in range(m):
        if M[i] not in t:
            break
        if i==m-1:
            cnt += 1

K, m= map(int,input().split())
if m==0:
    print(10**K)
else:
    M= list(input().split())
    A= [-1]*K
    cnt= 0
    perm(0)
    print(cnt)
