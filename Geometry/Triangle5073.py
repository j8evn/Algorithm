while True:
    n= list(map(int,input().split()))
    if sum(n)==0:
        break
    n.sort()
    if n[0]+n[1]<=n[2]:
        print("Invalid")
    else:
        if n[0]==n[1]==n[2]:
            print("Equilateral")
        elif n[0]==n[1] or n[1]==n[2] or n[0]==n[2]:
            print("Isosceles")
        elif n[0]!=n[1]!=n[2]:
            print("Scalene")