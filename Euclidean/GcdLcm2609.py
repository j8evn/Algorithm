#공식처럼 외워서 사용

#유클리드 호제법: (40,18)->(4,18)->(4,2)->(0,2)
                                        # 최대공약수:2
def gcd(a,b):
    if (a<b):
        a,b=b,a
    while True:
        if (a%b==0):
            return b
        a,b=b,a%b
        
#두 수의 최소공배수: 두 수의 곱//두 수의 최대공약수
def lcm(a,b):
    g=gcd(a,b)
    return(a*b//g)

n,m=map(int,input().split())
print(gcd(n,m))
print(lcm(n,m))
