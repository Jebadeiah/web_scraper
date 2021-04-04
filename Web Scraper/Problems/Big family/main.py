# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

# Work with the 'first_family' and 'second_family' and create a new dictionary
extended_family = first_family
extended_family.update(second_family.items())
print(extended_family)
