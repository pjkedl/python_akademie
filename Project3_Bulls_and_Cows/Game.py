import random


def game_header():
    print('Hi there!')
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")


def number_generator():
    number = str(random.randint(1000,9999))
    generated_number = [int(x) for x in str(number)]
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


def bull_cow(counter, computer_list, my_list):
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
    elif bull == 4 and counter <= 7:
        print(f"Correct, you've guessed the right number in {counter} guesses! That's excellent performance.")
        exit()
    elif bull == 4 and counter in range(8, 15):
        print(f"Correct, you've guessed the right number in {counter} guesses! That's very good performance.")
        exit()
    elif bull == 4 and counter in range(16, 25):
        print(f"Correct, you've guessed the right number in {counter} guesses! That's not very good performance.")
        exit()
    elif bull == 4 and counter > 25:
        print(f"Correct, you've guessed the right number in {counter} guesses! You can do better.")
        exit()


def main():
    counter = 1
    game_header()
    computer_list = number_generator()
    while True:
        bull_cow(counter, ask_for_number(), computer_list)
        counter += 1
        print(counter)


main()
