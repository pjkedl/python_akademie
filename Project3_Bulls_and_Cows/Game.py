import random

def game_header():
    print('Hi there!')
    print("I've generated a random 4 digit number for you.")
    number = str(2019)
    generated_number = [int(x) for x in str(number)]
    # number = str(random.randint(1000,9999))
    print("Let's play a bulls and cows game.")
    return generated_number

def ask_for_number():
    while True:
        a = input('Enter a number:')
        try:
            a = int(a)
        except ValueError:
            print('Please enter 4 digit number only.')
            continue
        if a not in range(1000, 9999):
            print('Please enter number in range 1000 - 9999.')
        else:
            guess = [int(x) for x in str(a)]
            break
    return guess

computer_list = game_header()
my_list =  ask_for_number()
for index, item in enumerate(my_list):
    if item in computer_list:



