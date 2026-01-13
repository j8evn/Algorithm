import sys
input= sys.stdin.readline

S= input().strip()
R= []
ss= ""
for i in range(len(S)):
    ss += S[i]
    if i%10==9:
        R.append(ss)
        ss= ""
R.append(ss)
print("\n".join(R))