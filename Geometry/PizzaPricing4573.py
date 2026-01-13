import math
import sys
input= sys.stdin.readline

idx= 0
while True:
    n= int(input())
    if (n==0):
        break
    idx += 1
    mm= []
    for i in range(n):
        d, p= map(int,input().split())
        mm.append([p/(((d/2)**2)*math.pi)*100, d])
    mm.sort(key=lambda x:x[0])
    print("Menu {}: {}".format(idx, mm[0][1]))
