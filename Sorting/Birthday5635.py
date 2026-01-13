import sys
input= sys.stdin.readline

n= int(input())
B= []
for i in range(n):
    B.append(list(input().split()))
    B[i][1:4]= map(int,B[i][1:4])
B.sort(key=lambda x:x[1])
B.sort(key=lambda x:x[2])
B.sort(key=lambda x:x[3])
print(B[-1][0])
print(B[0][0])