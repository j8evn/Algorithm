def MakeKey(x,y):
    return x*2000000001+y

n= int(input())
p= []
dic= {}
for i in range(n):
    p.append(list(map(int,input().split())))
    k= MakeKey(2*p[i][0],2*p[i][1])
    dic[k]= 1
for i in range(n):
    for j in range(i+1,n):
        k= MakeKey(p[i][0]+p[j][0],p[i][1]+p[j][1])
        dic[k]= dic.get(k,0)+ 2
print(max(dic.values()))
