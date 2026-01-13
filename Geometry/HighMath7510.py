T= int(input())
for i in range(T):
    n= list(map(int,input().split()))
    n.sort()
    if (n[0]**2+n[1]**2)==n[2]**2:
        print("Scenario #{:d}: \nyes\n".format(i+1))
    else:
        print("Scenario #{:d}: \nno\n".format(i+1))