import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    aa= list(input().split())
    if aa[1]=='jaehak' and aa[2]=='notyet' and (int(aa[3])==-1 or int(aa[3])>3):
        aa[4]= int(aa[4])
        A.append(aa)
A.sort(key=lambda x:x[4])

B= []
if len(A)>10:
    for i in range(10):
        B.append(A[i][0])
else:
    for i in range(len(A)):
        B.append(A[i][0])
B.sort()
print(len(B))
print(*B, sep="\n")