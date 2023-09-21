# -*- coding: utf-8 -*-


import random as rn


value = rn.randint(0, 100)
print("Generated Number ",value)

attempts = 100
print("Total attempts",attempts)

while True:
    
    print("Attempts remaining: ",attempts)
    guess = int(input('Guess a number: '))
 
    attempts -= 1

    if value > guess:
        print('Number is less than the generated number')
    elif value < guess:
        print('Number is greater than the generated number')
    else:
        print('You guessed it right in', 100-attempts, 'attempts!')
        break 
        
    value = rn.randint(0, 100)
    print(value)
    


