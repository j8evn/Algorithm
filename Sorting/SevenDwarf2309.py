H= []
for _ in range(9):
    H.append(int(input()))
H.sort()
a= sum(H)-100
for i in range(9):
    for j in range(i,9):
        if H[i]+H[j]==a:
            H.pop(i)
            H.pop(j-1)
            break
    if len(H)==7:
        break
H= map(str,H)
print('\n'.join(H))