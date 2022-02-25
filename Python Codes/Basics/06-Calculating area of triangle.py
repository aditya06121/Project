from cmath import sqrt


x = float(input("Enter Side:"))
y = float(input("Enter Side:"))
z = float(input("Enter Side:"))
s = (x+y+z)/2
a = sqrt(s*(s-x)*(s-y)*(s-z))
a = a.real
print(a)