import sys
input=sys.stdin.readline

a=[]
for i in range(5):
    a.append(int(input()))
a.sort(reverse=True)
avg=sum(a)//5
print(avg)
print(a[2])
