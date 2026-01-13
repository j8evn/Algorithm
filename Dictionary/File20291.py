import sys
input= sys.stdin.readline

N= int(input())
dic= {}
for i in range(N):
    s= input().strip()
    for j in range(len(s)):
        if s[j]=='.':
            if s[j+1:] in dic:
                dic[s[j+1:]] += 1
            else:
                dic[s[j+1:]]= 1
            break
dic= sorted(dic.items(), key=lambda x:x[0])
for i in range(len(dic)):
    print(dic[i][0],dic[i][1])