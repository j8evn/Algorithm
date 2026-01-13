n= int(input())
que, A= [], []
for i in range(n):
    que.append(i+1)
while len(que)!=1:
    A.append(que.pop(0))
    que.append(que.pop(0))
A.append(que.pop(0))
A= map(str,A)
print(' '.join(A))