N= int(input())
F= int(input())
for i in range(100):
    t= list(str(N))
    t.pop()
    t.pop()
    if i<10:
        t.append('0')
        t.append(str(i))
    else:
        t.append(str(i))
    t= ''.join(t)
    if int(t)%F==0:
        print(t[len(t)-2:])
        break