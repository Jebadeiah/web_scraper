import random


words = ['python', 'java', 'kotlin', 'javascript']
word = words[random.randint(0, 3)]
hint = ""

for i in word[0:3]:
    hint += i

hint += ('-' * (len(word) - 3))

print("H A N G M A N")
guess = input("Guess the word {}: ".format(hint))
if guess == word:
    print("You survived!")
else:
    print("You lost!")
