import sys
input= sys.stdin.readline

name= input()
N= int(input())
mm= -1
for _ in range(N):
    team= input().strip()
    t= team + name
    cnt= [t.count("L"), t.count("O"), t.count("V"), t.count("E")]
    cal= ((cnt[0]+cnt[1])*(cnt[0]+cnt[2])*(cnt[0]+cnt[3])*(cnt[1]+cnt[2])*(cnt[1]+cnt[3])*(cnt[2]+cnt[3]))%100
    if mm < cal:
        mm= cal
        ans= team
    elif mm == cal:
        if ans > team:
            ans= team
print(ans)