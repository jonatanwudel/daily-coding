'''
dice roll generator
'''
import random
print('Welcome to dice roll generator')

def main():
    number_dice = int(input('How many dice should I generate? '))
    dice_roll(number_dice)
    play_again()

def play_again():
    play_again = int(input('Insert 0 to exit, Insert 1 to play again: '))
    if play_again == 0: return print('Have a good day')
    elif play_again == 1: return main()
    else: print('Invalid')

def dice_roll(number_dice):
    dice = []
    for i in range(0, number_dice):
        dice.append(random.randint(1,6))
    return print('Result: ',*dice)

if __name__ == '__main__':
    main()