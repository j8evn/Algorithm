import sys
input= sys.stdin.readline

N, M= map(int,input().split())
A, dic= [], {}
for i in range(N):
    A.append(input().strip())
    dic[A[i]]= i+1

R= []
for _ in range(M):
    tt= input().strip()
    if tt.isdigit()==True:
        R.append(A[int(tt)-1])
    else:
        R.append(str(dic[tt]))
print('\n'.join(R))