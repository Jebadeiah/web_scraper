from typing import List

g_list: List[str] = []

while True:
    person = input()
    if person == '.':
        break
    else:
        g_list.append(person)

print(g_list)
print(len(g_list))
