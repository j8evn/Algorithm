R=int(input())
N=int(input())
S=0
for i in range(N):
    a,b=map(int, input().split())
    S=S+a*b
if (R==S):
    print("Yes")
else:
    print("No")
