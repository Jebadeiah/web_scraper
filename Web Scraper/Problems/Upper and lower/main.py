some_iterable = input().split()

new_dict = {key.upper(): key.lower() for key in some_iterable}
print(new_dict)
