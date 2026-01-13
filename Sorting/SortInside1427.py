N=list(map(int,input()))
A,B=[],[]

for i in range(len(N)):
    A.append(N[i])
A.sort()
for i in range(len(N)-1,-1,-1):
    B.append(A[i])
B=list(map(str,B))
print(''.join(B))

# 내림차순 정렬: A.sort(reverse=True)
