n, s= input().split()
n= int(n)
r= ""
for i in range(n):
    r += chr((ord(s[i])+(2**i%26))%ord('A')%26+ord('A'))
print(r)