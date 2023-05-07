'''
rock paper scissors
'''
import random


def main():
    rcp = ['rock','paper','scissors']
    print('Welcome to rock paper scissors game.')
    computer_choice = random.choice(rcp)
    #print(computer_choice)
    game(computer_choice)
    play_again()


def game(computer_choice):
    while True:
        user_choice = input('Write your choice: \"paper\", \"rock\", \"scissors\": ')
        if user_choice == computer_choice:
            print('Draw')
            break
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('Paper beat rock and you won!')
            break
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('Rock beat scissors and you won!')
            break
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('Scissors beat paper and you won!')
            break
        else:
            print('Computer win')
            break

def play_again():
    play_again = int(input('Insert 0 to exit, Insert 1 to play again: '))
    if play_again == 0: return print('Have a good day')
    elif play_again == 1: return main()
    else: return print('Invalid number')

if __name__ == '__main__':
    main()