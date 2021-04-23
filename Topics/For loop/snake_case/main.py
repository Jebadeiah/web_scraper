word = input()
ret = ""
for letter in word:
    if letter == word[0]:
        ret += letter.lower()
    elif letter.islower():
        ret += letter
    else:
        ret += f'_{letter.lower()}'

print(ret)
