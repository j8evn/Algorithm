import sys
input= sys.stdin.readline

n= int(input())
A= list(input().split())
dic= {}
for i in range(n):
    dic[A[i]]= 0
for _ in range(n):
    tt= list(input().split())
    for i in range(len(tt)):
        dic[tt[i]] += 1

dic= dict(sorted(dic.items(), key=lambda x:x[0]))
dic= sorted(dic.items(), key=lambda x:-x[1])
for d in dic:
    a, b= d
    print(a, b)