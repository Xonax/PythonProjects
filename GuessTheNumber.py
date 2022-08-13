#easy(1/30/medium(1/100)/hard(1/1000)

def easy():
    print('easy')
def medium():
    print('medium')
def hard():
    print('hard')
print('What level do you want to play?')
while True:
    lvl = input('easy(1/30/medium(1/100)/hard(1/1000): ').upper
    if lvl in ('EASY', 'MEDIUM', 'HARD'):
        print('You chose level: %s' % (lvl))
        if lvl == 'EASY':
            easy()
    else:
        print('Invalid Input')