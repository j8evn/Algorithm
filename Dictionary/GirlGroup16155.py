import sys
input= sys.stdin.readline

N, M= map(int,input().split())
dic= {}
for _ in range(N):
    s= input().strip()
    dic[s]= []
    n= int(input())
    for i in range(n):
        dic[s].append(input().strip())

for _ in range(M):
    t1= input().strip()
    t2= int(input())
    if t2==0:
        print('\n'.join(sorted(dic[t1])))
    else:
        for d in dic:
            if t1 in dic[d]:
                print(d)