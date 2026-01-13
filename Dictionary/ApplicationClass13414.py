import sys
input= sys.stdin.readline

K, L= map(int,input().split())
dic= {}
for _ in range(L):
    s= input().strip()
    if s in dic:
        dic.pop(s)
        dic[s]= 1
    else:
        dic[s]= 1

R= list(dic.keys())
if K<len(R):
    for i in range(K):
        print(R[i])
else:
    for i in range(len(R)):
        print(R[i])