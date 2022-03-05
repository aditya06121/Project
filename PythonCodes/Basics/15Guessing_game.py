import random


x = [1,2,3,4,5,6,7,8,9,10]
y = random.choice(x)
guess = int(input('Guess: '))
i = 1
while i < 3:
    if guess == y:
        print('You guessed correctly')
        break
    else:
        guess = int(input('Guess: '))
    i = i + 1
else:
    print("you guessed incorrectly")