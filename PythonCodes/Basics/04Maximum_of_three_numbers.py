x = int(input("Enter a No: "))
y = int(input("Enter another No: "))
z = int(input("Enter another No: "))

def comparison_3():
    if x>y:
        if x>z:
            return(x)
        else:
            return(z)
    elif y>x:
        if y>z:
            return(y)
        else:
            return(z)
    elif x == y:              #elif statement applied later due to x = z error handeling
        if x < z:
            return(z)
        else:
            return(x)
    else:
        return("All of em are equal")

print(comparison_3())