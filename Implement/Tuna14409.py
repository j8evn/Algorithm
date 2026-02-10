import sys
input= sys.stdin.readline

N= int(input())
X= int(input())
value= 0
i= 0
while i<N:
    p= list(map(int,input().split()))
    if len(p)==1:
        i -= 1
    else:
        if abs(p[0]-p[1])<=X:
            value += max(p[0],p[1])
        else:
            value += int(input())
        i += 1
print(value)