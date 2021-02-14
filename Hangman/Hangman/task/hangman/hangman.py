import random

words = ['python', 'java', 'kotlin', 'javascript']
word = words[random.randint(0, 3)]
guesses = set()


def hangman():
    tries = 8
    while tries > 0:
        hint = ''
        for i in word:
            if i in guesses:
                hint += i
            else:
                hint += '-'
        print()
        print(hint)
        if hint == word:
            print("You guessed the word!")
            print("You survived!")
            break
        print("Input a letter: >")
        guess = input()
        if not guess.islower() or len(guess) != 1:
            if not guess.islower():
                print("Please enter a lowercase English letter")
            if len(guess) != 1:
                print("You should input a single letter")
        elif guess in guesses:
            print("You've already guessed this letter")
        elif guess in word:
            guesses.add(guess)
        else:
            guesses.add(guess)
            tries -= 1
            print("That letter doesn't appear in the word")
            if tries == 0:
                print('You lost!')
                break

while True:
    print("H A N G M A N")
    print('Type "play" to play the game, "exit" to quit: ')
    game_start = input()
    if game_start.lower() == 'play':
        hangman()
    elif game_start.lower() == 'exit':
        break
    else:
        print('Please enter a valid argument\n')
