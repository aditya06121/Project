num = int(input("Enter a No:"))
if num<0:
    print("Their is no factorial of -ve numbers")
elif num == 0:
    print(1)
else:
    factorial = 1
    n = num
    while n > 1:
        factorial = factorial*n
        n = n-1
    print(factorial)

