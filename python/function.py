# This code is to learn Python by Andre Gonzaga
# This code is the simulator for Rock, Paper, Scissor
import random

def print_options():
    print('Lets play this... ')
    print('')
    print(' Rock ')
    print(' Paper ')
    print(' Scissor ')
    print('')

def ask_option():
    user_option=input('Your option now is: ')
    return user_option.lower()


def robot():
    options=['rock','paper','scissor']
    robot_option=random.choice(options)
    print('The computer chooses {}' .format(robot_option))
    return robot_option

def user_rock(user_option,robot_option):
    if robot_option == 'paper':
        print('The computer wins!')
    else:
        print('You win!!')


def user_paper(user_option,robot_option):
    if robot_option == 'rock':
        print('You win!!')
    else:
        print('The computer wins!')

def user_scissor(user_option,robot_option):
    if robot_option == 'rock':
        print('The computer wins!')
    else:
        print('You win!!')

def check_win(user_option,robot_option):
    if user_option == robot_option:
        print('The game draw')
    else:
        if user_option == 'rock':
            user_rock(user_option,robot_option)
        elif user_option == 'paper':
            user_paper(user_option,robot_option)
        elif user_option == 'scissor':
            user_scissor(user_option,robot_option)
        else:
            print('User choose wrong option')

def check_continue():
    import os
    play=input('Do you wish to play again: ')
    os.system('clear')
    return play

play = 'y'
while play != 'n':
    print_options()
    user_option=ask_option()
    robot_option=robot()
    check_win(user_option,robot_option)
    play=check_continue()

