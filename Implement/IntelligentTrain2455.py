p= 0
mm= -1
for i in range(4):
    Out, In= map(int,input().split())
    p -= Out
    p += In
    mm= max(mm,p)
print(mm)
