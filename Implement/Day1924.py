M1= [1,3,5,7,8,10,12]
M2= [4,6,9,11]
D= ["SUN","MON","TUE","WED","THU","FRI","SAT"]

x, y= map(int,input().split())
d= 0
for i in range(1,x+1):
    if i==x:
        d += y
    elif i in M1:
        d += 31
    elif i in M2:
        d += 30
    else:
        d += 28
print(D[d%7])