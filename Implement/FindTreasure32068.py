import sys
input= sys.stdin.readline

T= int(input())
for i in range(T):
    L, R, S= map(int,input().split())
    mm= min(2*(S-L),2*(R-S)-1)
    print(mm+1)