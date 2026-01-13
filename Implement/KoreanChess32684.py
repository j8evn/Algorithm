C= list(map(int,input().split()))
H= list(map(int,input().split()))
c, h= 72, 73.5
s= [13,7,5,3,3,2]
for i in range(6):
    c += C[i]*s[i]
    h += H[i]*s[i]
if c>h:
    print("cocjr0208")
else:
    print("ekwoo")