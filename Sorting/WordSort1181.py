import sys
input= sys.stdin.readline

n= int(input())
w= set()
for i in range(n):
    w.add(input().strip())
w= list(w)
n= len(w)
w.sort(key=lambda x:len(x))
s= []
ans= []
for i in range(n):
    if len(s)==0:
        s.append(w[i])
    elif(len(s)!=0 and len(s[-1])==len(w[i])):
        s.append(w[i])
    elif(len(s)!=0 and len(s[-1])!=len(w[i])):
        for j in range(len(s[-1])-1,-1,-1):
            s.sort(key=lambda x:ord(x[j]))
        for j in range(len(s)):
            ans.append(s[j])
        s= [w[i]]
if len(s)==1:
    ans.append(s[-1])
elif len(s)>1:
    for i in range(len(s[-1])-1,-1,-1):
        s.sort(key=lambda x:ord(x[i]))
    for i in range(len(s)):
        ans.append(s[i])
print("\n".join(ans))