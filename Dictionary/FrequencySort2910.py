N, C= map(int,input().split())
A= list(map(int,input().split()))

dic= {}
for i in range(N):
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]]= 1
dic= sorted(dic.items(), key=lambda x:x[1], reverse=True)

R= []
for i in range(len(dic)):
    for _ in range(dic[i][1]):
        R.append(dic[i][0])
R= map(str,R)
print(' '.join(R))