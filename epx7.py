import math;
a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
print("difference is ",abs(a-b))
if abs(a-b)<0.001:
    print("close")
else:
    print("not close")
