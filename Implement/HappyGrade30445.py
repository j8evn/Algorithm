happy= set(list("HAPPY"))
sad= set(list("SAD"))
hcnt, scnt= 0, 0

ss= input()
for i in range(len(ss)):
    if((ss[i] in happy)==True):
        hcnt+= 1
    if((ss[i] in sad)==True):
        scnt+= 1
        
if(hcnt+scnt==0):
    print("50.00")
else:
    t= 100*hcnt/(hcnt+scnt) # 파이썬에서 반올림할 때 주의
    t= int(t*1000)
    if(t%10>=5):
        t= t//10+1
    else:
        t= t//10
    t= t/100
    print("%.2f"%t)
