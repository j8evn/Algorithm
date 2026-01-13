import math

A1, P1= map(int,input().split())
R1, P2= map(int,input().split())
A2= R1*R1*math.pi
if P1/A1 < P2/A2:
    print("Slice of pizza")
else:
    print("Whole pizza")