num = int(input("Enter a No: "))

def factorial():
    if num<0:
        return("Their is no factorial of -ve numbers")
    elif num == 0:
        return(1)
    else:
        factorial = 1
        n = num
        while n > 1:
            factorial = factorial*n
            n = n-1
        return(factorial)

print(factorial())