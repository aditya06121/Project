#test_nbr = int(input('Enter the number: '))
def prime_test(test_nbr):
    factor = test_nbr // 2
    while factor > 1:
        if test_nbr % factor == 0:
            return(f'{test_nbr} is not prime, HCF of {test_nbr} is {factor}')
        factor -= 1
    else:
        return(f'{test_nbr} is prime')

print(prime_test(6))