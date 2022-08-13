#MADE BY LUCAS
import random

print('1.Best out of 3')
print('2.One game')

items = ['Rock', 'Paper', 'Scissors']

PlayerScore = 0
ComputerScore = 0
Game = 0

def Rock():
    global PlayerScore
    global ComputerScore
    if ComputerItem == 'Scissors':
        PlayerScore += 1
        print('You won score is: %s-%s Round: %s' % (PlayerScore, ComputerScore, Game))
    else:
        ComputerScore += 1
        print('You lost score is: %s-%s Round: %s' % (PlayerScore, ComputerScore, Game))
def Paper():
    global PlayerScore
    global ComputerScore
    if ComputerItem == 'Scissors':
        ComputerScore += 1
        print('You lost score is: %s-%s Round: %s' % (PlayerScore, ComputerScore, Game))
    else:
        PlayerScore += 1
        print('You won score is: %s-%s Round: %s' % (PlayerScore, ComputerScore, Game))
def Scissors():
    global PlayerScore
    global ComputerScore
    if ComputerItem == 'Paper':
        PlayerScore += 1
        print('You won score is: %s-%s Round: %s' % (PlayerScore, ComputerScore, Game))
    else:
        ComputerScore += 1
        print('You lost score is: %s-%s Round: %s' % (PlayerScore, ComputerScore, Game))

#Checks who won and prints it
if PlayerScore == 2:
    print('You Won with %s-%s' % (ComputerScore, PlayerScore))
if ComputerScore == 2:
    print('You lost with %s-%s' % (ComputerScore, PlayerScore))

while True:
    choice = input('What would you like to play?: ')
    if choice in ('1', '2'):
        if choice == '1':
            PlayerScore = 0
            ComputerScore = 0
            Game = 0
            #while gamecount is smaller or equel to 3 run code below
            while ComputerScore != 2 and PlayerScore != 2: 
                #Gives player player option to choose item and randomly picks computers item and prints it
                item = input('Choose your item: (Rock/Paper/Scissors or Cancel) ')
                if item in ('Rock', 'Paper', 'Scissors', 'Cancel'):
                    if item == 'Cancel':
                        break

                    ComputerItem = random.choice(items)
                    print('You chose %s!' % (item))
                    print('Computer chose %s!' % (ComputerItem))


                    
                    #checks if it is a tie if not plus 1 gamecount
                    if item == ComputerItem:
                        Game += 1
                        print('You Tied!')

                    #Checks which item the player chose
                    elif item == 'Rock':
                        Game += 1
                        Rock()
                    elif item == 'Paper':
                        Game += 1
                        Paper()
                    elif item == 'Scissors':
                        Game += 1
                        Scissors()
                        
                else:
                    print('Invalid input')
    else:
        print('Invalid input')
                
            