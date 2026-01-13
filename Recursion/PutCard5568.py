def perm(n):
    if (n==K):
        Eval()
        return
    for i in range(N):
        if V[i]==False:
            V[i]= True
            A[n]= i
            perm(n+1)
            V[i]= False

def Eval():
    t = []
    for i in range(K):
        t.append(B[A[i]])
    t= map(str,t)
    S.add(''.join(t))

N= int(input())
K= int(input())
A, V= [-1]*K, [False]*N
B= []
for _ in range(N):
    B.append(input().strip())
S= set()
perm(0)
print(len(S))