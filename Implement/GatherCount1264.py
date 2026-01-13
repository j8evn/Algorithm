import sys
input= sys.stdin.readline

a= ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
while True:
    ss= input().rstrip()
    if ss=="#":
        break
    cnt= 0
    for i in range(len(ss)):
        if ss[i] in a:
            cnt += 1
    print(cnt)