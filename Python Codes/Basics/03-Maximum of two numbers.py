def comparison_2():
    x = int(input("Enter a No: "))               #defining inputs
    y = int(input("Enter another No: "))
    if x == y:
        return("Both of em are equal")
    elif y<x:
        return(x)    
    else:
        return(y)


print(comparison_2())                        #recalling function