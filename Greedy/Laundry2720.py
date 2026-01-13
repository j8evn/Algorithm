n= [25, 10, 5, 1]
t= int(input())
for _ in range(t):
    c= int(input())
    r= []
    for i in range(len(n)):
        r.append(c//n[i])
        c= c%n[i]
    r= map(str,r)
    print(' '.join(r))