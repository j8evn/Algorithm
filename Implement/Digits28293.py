#상용로그로 자릿수 구하기:
#a**b가 매우 큰 수일 때 상용로그를 취함.
#c=a**b -> log10(c)=b*log10(a)
#log10(c)+1이 자릿수가 됨.

import math #math 모듈 사용
a,b=map(int,input().split())
aa=b*math.log10(a)
print(int(aa)+1)

'''
a,b=map(int,input().split())
s=a**b
print(len(str(s)))
''' #시간초과 (거듭제곱 구하는 게 시간이 오래걸림)
