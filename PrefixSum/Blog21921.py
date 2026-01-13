N, X= map(int,input().split())
A= list(map(int,input().split()))
for i in range(1,N):
    A[i]= A[i]+ A[i-1]
A.insert(0,0)

S= []
for i in range(N-X+1):
    S.append(A[i+X]-A[i])

mm= max(S)
cnt= 0
for i in range(len(S)):
    if S[i]==mm:
        cnt += 1
if mm==0:
    print("SAD")
else:
    print(mm)
    print(cnt)