k= int(input())
s= 0
n= k%5
k= k//5 +1
for i in range(k):
    s += (30*i)*5
s += 30*(i+1)*n
print(s)