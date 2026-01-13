def Bitten(e):
    cnt = 0
    t = e%(p1+r1)
    if (t<=p1 and t!=0):
        cnt = cnt + 1
    t = e%(p2+r2)
    if (t<=p2 and t!=0):
        cnt = cnt + 1
    return cnt

p1, r1, p2, r2 = map(int,input().split())
p, m, n = map(int,input().split())

print(Bitten(p))
print(Bitten(m))
print(Bitten(n))
