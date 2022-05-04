import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess between 1 and {x}: '))
        if guess < random_number:

            print('Cold - Number Too Low')
        elif guess > random_number:
            print('Hot - Number too High')

    print(f'You got it. You guessed the number {random_number}')


def computer_guess(x):
    low_g = 1
    high_g = x
    result = ''
    attempts = 0
    while result != 'c':
        if low_g != high_g:
            guess = random.randint(low_g, high_g)
        else:
            guess = low_g
        result = input(
            f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if result == 'h':
            low_g = guess - 1
            attempts += 1
        elif result == 'l':
            low_g = guess + 1
            attempts += 1

    print(f'Computer guessed correctly: {guess} in {attempts} many attempts')


computer_guess(10)
