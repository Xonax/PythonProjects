#easy(1/30/medium(1/100)/hard(1/1000
import random
min = 1
max = 2

def easy():
    global max
    max = 30
    randomNumber = random.randrange(min,max)

    while True:
        guess = float(input('Choose a number between 1 and %s: ' % (max)))
        if guess == randomNumber:
            print('Goodjob you guessed the number!')
            Start()
            break

        if randomNumber<(guess+(max/5)) and randomNumber>(guess-(max/5)):
            print('Warm')
        else:
            print('Cold')


def medium():
    global max
    max = 100
    randomNumber = random.randrange(min,max)
    while True:
        guess = float(input('Choose a number between 1 and %s: ' % (max)))
        if guess == randomNumber:
            print('Goodjob you guessed the number!')
            Start()
            break

        if randomNumber<(guess+(max/5)) and randomNumber>(guess-(max/5)):
            print('Warm')
        else:
            print('Cold')

def hard():
    global max
    max = 1000
    randomNumber = random.randrange(min,max)
    while True:
        guess = float(input('Choose a number between 1 and %s: ' % (max)))
        if guess == randomNumber:
            print('Goodjob you guessed the number!')
            Start()
            break

        if randomNumber<(guess+(max/5)) and randomNumber>(guess-(max/5)):
            print('Warm')
        else:
            print('Cold')

print('What level do you want to play?')
def Start():
    lvl = input('easy(1/30/medium(1/100)/hard(1/1000): ').upper()
    if lvl in ('EASY', 'MEDIUM', 'HARD'):
        print('You chose level: %s' % (lvl))
        if lvl == 'EASY':
            easy()
        if lvl == 'MEDIUM':
            medium()
        if lvl == 'HARD':
            hard()
    else:
        print('Invalid Input')
Start()