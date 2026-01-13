import math

L= int(input())
a= math.sqrt((L*2)**2-L*L)
print(min(L*a,1/4*a*math.sqrt(4*(L*L)-a*a)))