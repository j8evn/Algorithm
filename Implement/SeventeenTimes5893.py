N= list(input().strip())
N.reverse()
d, b= 0, []
for i in range(len(N)):
    if N[i]=='1':
        d += 2**i
d= d*17
while (d>0):
    b.append(d%2)
    d= d//2
b.reverse()
b= map(str,b)
print(''.join(b))
