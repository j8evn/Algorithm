n, k= map(int,input().split())
que, A= [], []
for i in range(n):
    que.append(i+1)
while que:
    for i in range(k-1):
        que.append(que.pop(0))
    A.append(que.pop(0))
A= map(str,A)
print("<"+', '.join(A)+">")