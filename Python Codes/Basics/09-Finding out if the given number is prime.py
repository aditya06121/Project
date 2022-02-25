test_nbr = int(input('Enter the number: '))
factor = test_nbr // 2
while factor > 1:
    if test_nbr % factor == 0:
        print(f'{test_nbr} is not prime')
        print(f'HCF of {test_nbr} is {factor}')
        break
    factor -= 1
else:
    print(f'{test_nbr} is prime')