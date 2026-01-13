import sys
input= sys.stdin.readline

def Bsearch(e):
    l, u = 0, len(A)-1
    while (l<=u):
        mid = (l+u)//2
        if (A[mid] == e):
            return "1"
        elif (e>A[mid]):
            l = mid+1
        else:
            u = mid-1
    return "0"

T= int(input())
for _ in range(T):
    N= int(input())
    A= list(map(int,input().split()))
    M= int(input())
    B= list(map(int,input().split()))
    A.sort()
    R= []
    for i in range(M):
        R.append(Bsearch(B[i]))
    print('\n'.join(R))