S= -1
for _ in range(3):
    s= input()
    if s!="FizzBuzz" and s!="Fizz" and s!="Buzz":
        S= int(s)
    elif S!=-1:
        S += 1

S= S+ 1
if S%3==0 and S%5==0:
    print("FizzBuzz")
elif S%3==0:
    print("Fizz")
elif S%5==0:
    print("Buzz")
else:
    print(S)