import sys
input=sys.stdin.readline

K=int(input())
c=0
for i in range(K):
    k=[]
    c+=1
    C=list(map(int,input().split()))
    N=C[0]
    del C[0]
    C.sort(reverse=True)
    for j in range(N-1):
       k.append(C[j]-C[j+1])
    print("Class %d" % c)
    print("Max", "%d," % max(C), "Min", "%d," % min(C), "Largest gap %d" % max(k))

