import random
import itertools

def game_header():
    print('Hi there!')
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")


def number_generator():
    generated_number = [int(x) for x in range(10)]
    secret = []

    for i in generated_number:
        number = random.choice(generated_number)
        if len(secret) == 4:
            break
        else:
            secret.append(number)
            generated_number.remove(number)
    return secret


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


def evaluate_performance(counter):
    if counter <= 7:
        return "That's excellent performance"
    elif counter <= 15:
        return "That's very good performance"
    elif counter <= 25:
        return "That's not very good performance"
    else:
        return "You can do better"


def bull_cow(counter, guess, secret):
    bull = 0
    cow = 0
    for index, item in enumerate(guess):
        if item in secret:
            if secret[index] == guess[index]:
                bull += 1
            else:
                cow += 1
    if bull != 4:
        print(f'{bull} bulls, {cow} cows')
    else:
        print(f"Correct, you've guessed the right number in {counter} guesses! {evaluate_performance(counter)}")
        return True


def main():
    game_header()
    secret = number_generator()
    for counter in itertools.count(1):
        if bull_cow(counter, ask_for_number(), secret) == True:
            break
    exit()

main()
