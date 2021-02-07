import random


words = ['python', 'java', 'kotlin', 'javascript']
word = words[random.randint(0, 3)]
hint = ('-' * (len(word)))
tries = 8


print("H A N G M A N")
while tries > 0:
    print(hint)
    guess = input("Input a letter")
    if guess in word:
        word.replace()
        print("You survived!")
    else:
        tries -= 1
        print("Whoops! Only {} tries left!".format(tries))

print("You're trash! You're garbage!")
