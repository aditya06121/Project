from cmath import sqrt


x = float(input("Enter Side: "))
y = float(input("Enter Side: "))
z = float(input("Enter Side: "))

def area():
    s = (x+y+z)/2
    a = sqrt(s*(s-x)*(s-y)*(s-z))
    a = a.real              #for removing imaginay part of a, using sqrt function gives variable a imaginary part
    return(a)

print(area())