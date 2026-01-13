L = input().strip()
ll = len(L)//3
L1, L2, L3 = L[:ll], L[ll:ll*2], L[ll*2:]
if (L1==L2):
    print(L1)
elif (L2==3):
    print(L2)
else:
    print(L3)
