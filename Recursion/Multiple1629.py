# 나머지 분배 법칙: (A*B)%C = ((A%C)*(B%C)) %C
# A^B%C = (A^(B//2) * A^(B//2)) %C (짝수)
# A^B%C = (A^(B//2) * A^(B//2) * A) %C (홀수)

def f(a,b,c): # 분할정복
    if b==1:
        return a%c
    tt= f(a,b//2,c)
    if b%2==0:
        return ((tt*tt)%c)%c
    else:
        return (((tt*tt)%c)*a)%c

A, B, C= map(int,input().split())
print(f(A,B,C))