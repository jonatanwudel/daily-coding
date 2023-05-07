'''
guess the number
'''
import random


def main():
    print('Welcome to \"Guess the number\" game.')
    computer_number = random.randrange(0,100)
    print('Computer chose random number between 0 and 100')
    #print(computer_number)
    game(computer_number)
    play_again()


def play_again():
    play_again = int(input('Insert 0 to exit, Insert 1 to play again: '))
    if play_again == 0: return print('Have a good day')
    elif play_again == 1: return main()
    else: return print('Invalid number')


def game(computer_number):
    guesses = []
    while True:
        user_guess = int(input("Your guess?: "))
        if user_guess == computer_number:
            guesses.append(user_guess)
            if len(guesses) != 0:
                print('Great job you only need ',len(guesses),' attempts')
                print(*guesses)
                break
            else:
                print('Wow, nice first try')
                break
        else:
            if user_guess > computer_number:
                print('It\'s lower')
                continue
            elif user_guess < computer_number:
                guesses.append(user_guess)
                print('It\'s higher')
                continue


if __name__ == '__main__':
    main()