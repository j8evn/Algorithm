n= list(map(int,input().split()))
k= []
for i in range(7):
    k.append(n[i]-n[i+1])
if k[0]==k[1]==k[2]==k[3]==k[4]==k[5]==k[6]==-1:
    print("ascending")
elif k[0]==k[1]==k[2]==k[3]==k[4]==k[5]==k[6]==1:
    print("descending")
else:
    print("mixed")
