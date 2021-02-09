import random


words = ['python', 'java', 'kotlin', 'javascript']
word = words[random.randint(0, 3)]
guesses = set()
tries = 8


print("H A N G M A N\n'll ")
while tries > 0:
    hint = ''
    for i in word:
        if i in guesses:
            hint += i
        else:
            hint += '-'
    print(hint)
    guess = input("Input a letter: ")
    print()
    if guess in word:
        tries -= 1
        guesses.add(guess)
    else:
        tries -= 1
        if tries == 0:
            break
        print("That letter doesn't appear in the word")

print('Thanks for playing!')
print("We'll see how well you did in the next stage")
