import math

n= int(input())
for _ in range(n):
    a, b, c= map(float,input().split())
    p= (-b+math.sqrt(b*b-4*a*c))/(2*a)
    m= (-b-math.sqrt(b*b-4*a*c))/(2*a)
    print("{:.3f}, {:.3f}".format(p,m))