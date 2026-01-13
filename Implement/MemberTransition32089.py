while True:
    n= int(input())
    if n==0:
        break
    N= list(map(int,input().split()))
    mm= -1
    for i in range(n-2):
        mm= max(mm, N[i]+N[i+1]+N[i+2])
    print(mm)