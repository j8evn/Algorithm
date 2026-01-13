import sys
input= sys.stdin.readline

N= int(input())
cnt, dic= {}, {}
for _ in range(N):
    p, s= input().split()
    if s=='-':
        continue
    if s in cnt:
        cnt[s] += 1
        dic[s].append(p)
    else:
        cnt[s]= 1
        dic[s]= [p]

R= []
for c in cnt:
    if cnt[c]==2:
        R.append(dic[c])
print(len(R))
for a, b in R:
    print(a, b)