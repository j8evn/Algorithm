import sys
input= sys.stdin.readline

n= int(input())
b= {}
for i in range(n):
    t= input().strip()
    if t in b:
        b[t] += 1
    else:
        b[t] = 1
mm= -1
for k in b.keys():
    if mm<b[k]:
        mm= b[k]
        s= k
    elif mm==b[k] and s>k:
        s= k
print(s)
