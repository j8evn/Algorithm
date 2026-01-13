while True:
    N= int(input())
    if N==0:
        break
    dic= {}
    for i in range(N):
        a, b= input().split()
        dic[a]= float(b)
    R= []
    mm= max(dic.values())
    for d in dic:
        if dic[d]==mm:
            R.append(d)
    print(' '.join(R))