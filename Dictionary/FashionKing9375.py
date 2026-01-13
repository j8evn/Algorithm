T= int(input())
for _ in range(T):
    dic= {}
    n= int(input())
    for i in range(n):
        a, b= input().split()
        if b not in dic:
            dic[b]= [a]
        else:
            dic[b].append(a)
    cnt= 0
    ll= 1
    for d in dic:
        ll= ll* (len(dic[d])+1)
    cnt += ll
    cnt -= 1
    print(cnt)
    