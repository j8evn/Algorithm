N= int(input())
for i in range(N):
    Y= []
    K= []
    for i in range(9):
        y, k= map(int,input().split())
        Y.append(y)
        K.append(k)
    if (sum(Y) > sum(K)):
        print("Yonsei")
    elif (sum(Y) < sum(K)):
        print("Korea")
    else:
        print("Draw")
