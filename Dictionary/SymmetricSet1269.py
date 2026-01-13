a, b= map(int,input().split())
A= list(map(int,input().split()))
B= list(map(int,input().split()))
dic= {}
for i in range(a):
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]]= 1
for i in range(b):
    if B[i] in dic:
        dic[B[i]] += 1
    else:
        dic[B[i]]= 1
cnt= 0
for d in dic:
    if dic[d]==1:
        cnt += 1
print(cnt)