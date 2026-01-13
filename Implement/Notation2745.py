# ord():10진수 유니코드로 변환
import sys
input=sys.stdin.readline

def IsDigit(c):
    if (ord(c)>=ord('0') and (ord(c)<=ord('9'))):
        return True     #10진수인지 판단
    else:
        return False
A=[]
t,a=input().split()
a = int(a)
for i in range(len(t)):
    if (IsDigit(t[i])==True):
        A.append(int(t[i]))
    else:
        A.append(ord(t[i])-ord('A')+10) # 10진수로 변환
# 진법 계산
A.reverse()
s,B=0,1
for i in range(len(A)):
    s=s+B*A[i]
    B=B*a
print(s)
