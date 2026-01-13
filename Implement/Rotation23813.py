N= list(input())
ss= 0
for k in range(len(N)):
    l= []
    for i in range(-k,len(N)-k):
        l.append(N[(i-1)%len(N)])
    ss += int(''.join(l))
print(ss)