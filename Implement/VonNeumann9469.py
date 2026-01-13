N = int(input())
for i in range(N):
    T, D, A, B, F = map(float,input().split())
print(T, D/(A+B)*F)
