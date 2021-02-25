ret = []
sentence = input().split()

for word in sentence:
    if word[-1].lower() == 's':
        ret.append(word)

print("_".join(ret))
