def sol():
    for x in range(-999,1000):
        for y in range(-999,1000):
            if (a*x+b*y!=c):
                continue
            if (d*x+e*y!=f):
                continue
            print(x,y)
            return
a,b,c,d,e,f=map(int,input().split())
sol()
