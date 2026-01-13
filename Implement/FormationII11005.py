N, B= map(int,input().split())
ss= []
while (N>0):
    ss.append(N%B)
    N= N//B
for i in range(len(ss)):
    if ss[i]>9:
        ss[i]= chr(ord('A')+ss[i]-10)
ss.reverse()
ss= map(str,ss)
print(''.join(ss))