import sys
input = sys.stdin.readline

n, s= map(int,input().split())
cnt, cur= 0, s
for i in range(n):
    k= input().strip()
    if (len(k)==2):
        a= int(k[0])+1
    else:
        a= int(k)
    if (cur<a):
        cur= s
        cnt+= 1
    cur-= a
print(cnt)
