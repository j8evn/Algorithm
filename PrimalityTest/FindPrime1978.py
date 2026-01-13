#number 변수가 1보다 클 경우, 2번째 for문으로 이동
#2부터 number-1 까지 범위에서 number를 나눔
#나머지가 0인 경우 no_prime 1증가
#no_prime이 0일 경우, prime 1 증가

n=int(input())
numbers=list(map(int,input().split()))
prime=0  #소수인 수의 개수

for number in numbers:
    no_prime=0  #소수가 아닌 수의 개수
    if (number>1):
        for i in range(2,number):
            if (number%i==0):
                no_prime+=1
        if (no_prime==0):
            prime+=1
print(prime)
