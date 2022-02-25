from cmath import sqrt


x = int(input("First Coefficient:"))
y = int(input("Second Coefficient:"))
z = int(input("Constant:"))
d = (y**2) - 4*x*z
if x == 0:
    print("Fuck")
else:
    if d >= 0:
        r1 = (-y+sqrt(d))/2*x
        r2 = (-y-sqrt(d))/2*x
        r1 = r1.real
        r2 = r2.real
        if r1 == r2:
            print(r1)
        else:
            print(r1,r2)
    else:
        r3 = (-y+sqrt(d))/2*x
        r4 = (-y+sqrt(d))/2*x
        print(r3,r4)
