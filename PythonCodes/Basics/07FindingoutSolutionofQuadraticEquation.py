from cmath import sqrt


x = int(input("First Coefficient: "))
y = int(input("Second Coefficient: "))
z = int(input("Constant: "))

def roots():
    d = (y**2) - 4*x*z
    if d == 0:
        r = -y / 2*x
        return(f'roots are equal {r}')
    else:
        if d >= 0:
            r1 = (-y+sqrt(d))/2*x
            r2 = (-y-sqrt(d))/2*x
            r1 = r1.real
            r2 = r2.real
            return(f'root1 is: {r1} and root2 is: {r2}')
        else:
            r3 = (-y+sqrt(d))/2*x
            break_list = (r3.real,r3.imag)  #breaking real and imaginary
            rr = r3.real
            ri = r3.imag
            r4 = (-y+sqrt(d))/2*x
            break_list2 = (r4.real,r4.imag)    #breaking real and imaginary
            rr2 = r4.real
            ri2 = r4.imag
            return(f'{rr2}+{ri2}i, {rr}+{ri}i')


print(roots())