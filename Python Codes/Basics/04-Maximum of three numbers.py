x = int(input("Enter a No:"))
y = int(input("Enter another No:"))
z = int(input("Enter another No:"))

if x>y:
    if x>z:
        print(x)
    else:
        print(z)
elif y>x:
    if y>z:
        print(y)
    else:
        print(z)
else:
    print("All of em are equal")