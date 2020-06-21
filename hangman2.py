# Write your code here
import random

random.seed = 10
print('H A N G M A N')

def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word_random = random.choice(word_list)
    print()
    print('-' * len(word_random))

    lives = 8


    def word_print():
        temp_find = ''
        for _ in word_random:
            if _ in letter_set:
                temp_find = temp_find + _
            else:
                temp_find = temp_find + '-'
        return temp_find


    letter_set = set()
    not_present = set()

    while lives > 0:
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print("You should input a single letter")
            print()
            print(word_print())
            continue
        if not letter.islower():
            print("It is not an ASCII lowercase letter")
            print()
            print(word_print())
            continue

        if letter in word_random:
            if letter not in letter_set:
                letter_set.add(letter)
            else:
                print("You already typed this letter")

        else:
            if letter not in not_present:
                not_present.add(letter)
                print("No such letter in the word")
                lives -= 1
            else:
                print("You already typed this letter")
        word_found = word_print()
        if word_found == word_random:
            print("You guessed the word!")
            print("You survived!")
            break
        if lives == 0:
            print("You are hanged!")
            break
        print()
        print(word_found)


while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        hangman()
    else:
        break