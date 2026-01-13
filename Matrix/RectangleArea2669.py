C= set()
for i in range(4):
    x1, y1, x2, y2= map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            ll= str(j)+str(k)
            C.add(ll)
print(len(C))

