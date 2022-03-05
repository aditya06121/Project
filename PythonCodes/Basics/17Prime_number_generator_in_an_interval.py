def primeno_gen():
    upr_limit = int(input('Enter Upper limit: '))
    lwr_limit = int(input('Enter Lower limit: '))
    numbers = []
    while upr_limit >= lwr_limit:
        factor = upr_limit // 2
        while factor > 1:
            if upr_limit % factor == 0:
                break
            factor -= 1
        else:
            numbers.append(upr_limit)
        upr_limit -= 1
    return(numbers)               #return should be outside of the loop because it immediatly stops the loop breaking the function


print(primeno_gen())