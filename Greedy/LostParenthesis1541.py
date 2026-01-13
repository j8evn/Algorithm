ss= input().strip()
p, m=  "", ""
r= 0
for i in range(len(ss)):
    if ss[i]=="-":
        if m!="":
            m= list(map(int,m.split("+")))
            r -= sum(m)
            m= "0"
        else:
            m += "0"
    else:
        if m=="":
            p += ss[i]
        else:
            m += ss[i]
if p:
    p= list(map(int,p.split("+")))
    r += sum(p)
if m:
    m= list(map(int,m.split("+")))
    r -= sum(m)
print(r)