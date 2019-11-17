import random

def game_header():
    print('Hi there!')
    print("I've generated a random 4 digit number for you.")
    number = str(2017)
    generated_number = [int(x) for x in str(number)]
    # number = str(random.randint(1000,9999))
    print("Let's play a bulls and cows game.")
    print(generated_number)
    return generated_number

def ask_for_number():
    while True:
        a = input('Enter a number:')
        try:
            a = int(a)
        except ValueError:
            print('Please enter number only.')
            continue
        if a not in range(1000, 9999):
            print('Please enter 4 digit number in range 1000 - 9999.')
        else:
            guess = [int(x) for x in str(a)]
            break
    return guess

def bull_cow(counter):
    computer_list = game_header()
    my_list = ask_for_number()
    bull = 0
    cow = 0
    for index, item in enumerate(my_list):
        if item in computer_list:
            if computer_list[index] == my_list[index]:
                bull += 1
            else:
                cow += 1
    if bull != 4:
        print(f'{bull} bulls, {cow} cows')
    else:
        print(f"Correct, you've guessed the right number in {counter} guesses!")
        exit()

def main():
    counter = 1
    game_header()
    while True:
        ask_for_number()
        bull_cow(counter)
        counter += 1

main()









