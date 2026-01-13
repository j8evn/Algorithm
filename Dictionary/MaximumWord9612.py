import sys
input= sys.stdin.readline

N= int(input())
dic= {}
for _ in range(N):
    ss= input().strip()
    if ss in dic:
        dic[ss] += 1
    else:
        dic[ss]= 1
dic= dict(sorted(dic.items(), key=lambda x:x[0], reverse=True))
dic= sorted(dic.items(), key=lambda x:-x[1])
for d in dic:
    a, b= d
    break
print(a,b)