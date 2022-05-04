import random
from words import words
from visuals import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    # use set to check off if all letters have beenm used
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('life counter: ', lives,
              ', and you have used these characters: ', ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        guessed_letter = input('Guess a letter: ').upper()
        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                print('')

            else:
                lives -= 1
                print('\nThe: ', guessed_letter, 'not in word')

        elif guessed_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died. The word was', word)
    else:
        print('YAY! You guessed the word', word, '. Good job')


if __name__ == '__main__':
    hangman()
