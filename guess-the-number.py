### guess the number

import random

def guess_the_number():

    print('Welcome to my number guessing game. Guess the number between 1 and 100.')
    number_to_guess = random.randint(1, 100)
    attempts = 0


    while True:
        try:
            your_guess = int(input('Please enter your guess here: '))
            attempts += 1

            if your_guess < 1 and your_guess > 100:
                print('Please enter a number between 1 and 100. ')
                continue

            elif your_guess > number_to_guess:
                print('Please try again. The number is too high.')

            elif your_guess < number_to_guess:
                print('Please try again. The number is too low.')

            else:
                print(f'Welcome. You guessed the number in {attempts} attempts.')
                break

        except ValueError:
            print('Invalid Choice. Please enter a valid number.')


if __name__ == "__main__":
    guess_the_number()


