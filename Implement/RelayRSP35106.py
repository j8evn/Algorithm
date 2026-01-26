N= int(input())
A= list(map(int, input().split()))
s= [0]*3
for i in range(len(A)):
    s[A[i]-1] += 1

res= [0, 0]
for i in range(3):
    if s[i]<N:
        res[1]= i+1
    if s[i]>N:
        res[0]= i+1
print(res[1])
print(res[0])