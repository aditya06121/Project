upr_limit = int(input('Enter Upper limit: '))
lwr_limit = int(input('Enter Lower limit: '))
while upr_limit >= lwr_limit:
    factor = upr_limit // 2
    while factor > 1:
        if upr_limit % factor == 0:
            break
        factor -= 1
    else:
        print(upr_limit)
    upr_limit -= 1