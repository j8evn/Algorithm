from collections import deque
import sys
input= sys.stdin.readline

def AC():
    rc= 0
    for i in range(len(p)):
        if p[i]=='R':
            rc += 1
        elif p[i]=='D':
            if X:
                if rc%2==0:
                    X.popleft()
                else:
                    X.pop()
            else:
                return "error"
    if rc%2==1:
        X.reverse()
    R= ["["]
    for i in range(len(X)):
        R.append(str(X[i]))
        R.append(",")
    if "," in R:
        R.pop()
    R.append("]")
    return "".join(R)

T= int(input())
for _ in range(T):
    p= input()
    n= int(input())
    s= input()
    s= s[1:-2]
    X= deque()
    if "," in s:
        X= deque(map(int,s.split(",")))
    elif len(s)!=0:
        X.append(int(s))
    print(AC())