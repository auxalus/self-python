#guessing game 
#generate random integer betn 1 to 100

import random
jackpot = random.randint(1,100)

guess = int(input('guess the number'))
counter = 1

# if guess == jackpot:
#     print('you win')
# else:
#     print('you lose')

while guess != jackpot:
    if guess < jackpot:
        print('guess higher')
    else:
        print('guess lower')
        
    guess = int(input('guess the number'))
    counter += 1

else:
    print('you win')
    print('attempts',counter)