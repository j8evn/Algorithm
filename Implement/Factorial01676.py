import math

N= int(input())
N= str(math.factorial(N))
cnt= 0
for i in range(len(N)-1,-1,-1):
    if N[i]=="0":
        cnt += 1
    else:
        break
print(cnt)