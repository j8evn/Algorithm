import math
import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    N= int(input())
    flag= False
    for i in range(1,int(math.sqrt(N))+1):
        if i*i==N:
            flag= True
            break
    if flag==False:
        print(0)
    else:
        print(1)