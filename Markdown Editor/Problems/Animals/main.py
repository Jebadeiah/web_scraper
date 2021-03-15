file = open("animals.txt", 'r+', encoding='utf-8')
new_file = open("animals_new.txt", 'w+', encoding='utf-8')
for animal in file.readlines():
    new_file.write(animal.replace('\n', ' '))
file.close()
new_file.close()
