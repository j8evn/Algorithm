n= int(input())
for i in range(n):
    ll= input().strip()
    ans= [ll[0]]
    for j in range(1,len(ll)):
        if ll[j] != ans[-1]:
            ans.append(ll[j])
            
    print(''.join(ans))
