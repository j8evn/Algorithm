import sys
input= sys.stdin.readline

N, M= map(int,input().split())
dic= {}
for _ in range(N):
    ss= input().strip()
    if len(ss) >= M:
        if ss in dic:
            dic[ss] += 1
        else:
            dic[ss]= 1

dic= dict(sorted(dic.items()))
dic= dict(sorted(dic.items(), key=lambda x:-len(x[0])))
dic= dict(sorted(dic.items(), key= lambda x:-x[1]))
print('\n'.join(list(dic.keys())))