import sys
input= sys.stdin.readline

N, M= map(int,input().split())
A= []
a, b= [], []
dic= {}
for i in range(N):
    dic[i+1]= 0

while True:
    tt= list(input().split())
    if tt[0]==tt[1]=='0':
        break
    tt[0]= int(tt[0])
    if dic[tt[0]]==M:
        continue
    if tt[0]%2==0:
        dic[tt[0]] += 1
        b.append(tt)
    else:
        dic[tt[0]] += 1
        a.append(tt)

a.sort(key=lambda x:x[1])
a.sort(key=lambda x:len(x[1]))
a.sort(key=lambda x:x[0])

b.sort(key=lambda x:x[1])
b.sort(key=lambda x:len(x[1]))
b.sort(key=lambda x:x[0])

for i in range(len(a)):
    print(*a[i])
for i in range(len(b)):
    print(*b[i])