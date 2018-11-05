# The task, read a game.
# Игра "угадай число" (проще)
# ValueError


import random

python = random.randint(1, 30)


print('System loading...')
print('Python: Hello, let\' play my game!')
print('If you win, then you will survive.')

print('''Rules: 
    I guessing a number, if you have guessed, then you won! Otherwise, you dead!
    You will have 4 lives ''')

health = 4

while health > 0:
    user_input = int(input('Enter a number. I recommend to think({} attempts): '.format(health)))

    if user_input == python:
        print('You win, congratulation!, number was {}. Thank you so much for the game, good luck!'.format(python))
        break
    elif user_input > python:
        print('System a number - Less')
        health -= 1
        if health == 0:
            print('You lose! You are out of attempts. Number was - ', python)
            break
        continue
    elif user_input < python:
        print('System a number - More')
        health -= 1
        if health == 0:
            print('You lose! You are out of attempts. Numbers was - ', python)
            break
        continue
