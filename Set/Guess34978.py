import sys
input= sys.stdin.readline

N= int(input())
X, Y= [], []
for _ in range(N):
    A= list(input().split())
    X.append(A[0])
    Y.append(set(A[2:]))
S= input().strip()

t= True
for i in range(N):
    for j in range(len(S)):
        if S[j]==X[i] and j+1 < len(S):
            if S[j+1] not in Y[i]:
                t= False
                break
print("yes" if t else "no")