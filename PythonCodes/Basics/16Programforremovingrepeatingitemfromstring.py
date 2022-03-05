x = [1,1,4,5,5,7,7,8,9,9,10]
y = [] # Empty list
for z in x: # z takes value from each element of x
    if z not in y:  # checks if the elements which z takes on belongs in list y
        y.append(z)  # z is added in y
print(y)