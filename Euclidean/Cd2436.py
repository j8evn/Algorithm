#찾아야 하는 두 자연수: A,B
#최대공약수 G는 A와 B의 공통 약수, 따라서 a와 b가 서로소일때, A=a*G, B=b*G
#최소공배수 L=a*b*G -> L/G=a*b
#서로소인 a와 b를 구하고 그 값들에 G를 곱하기 -> A,B

def gcd(a,b):
    if (a<b):
        a, b= b, a
    while True:
        if (a%b==0):
            return b
        a, b= b, a%b

G, L= map(int,input().split())
T= L//G
mm, A, B= 2*T, -1, -1
for a in range(1,T+1):
    b= T//a
    if (b<a): #a가 b보다 커지면 빠져나감
        break
    if (T%a!=0): #T=30일때 a=4라면 그 다음 a로 넘어감
        continue
    if (gcd(a,b)!=1): #서로소가 아니면 넘어감
        continue
#여기까지 오면 적법한 a,b임
    if (a+b<mm):
        mm, A, B= a+b, a, b
print(A*G,B*G)
