T= int(input())
for i in range(T):
    A= [False]*26
    ss= input().strip()
    for j in range(len(ss)):
        A[ord(ss[j])-ord('A')]= True
    h= 0
    for j in range(26):
        if (A[j]==False):
            h+= (j+ord('A'))
    print(h)
