T= int(input())
for i in range(T):
    tt= list(map(int,input().split()))
    tt.sort()
    if tt[0]+tt[1]<=tt[2]:
        print("Case #{:d}:".format(i+1), "invalid!")
        continue
    if tt[0]==tt[1]==tt[2]:
        print("Case #{:d}:".format(i+1), "equilateral")
    elif tt[0]==tt[1] or tt[1]==tt[2]:
        print("Case #{:d}:".format(i+1), "isosceles")
    else:
        print("Case #{:d}:".format(i+1), "scalene")