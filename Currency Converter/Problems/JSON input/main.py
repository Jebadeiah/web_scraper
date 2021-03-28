import json


initial_input = input()
with open("jason_file.json", "w") as the_input_yo:
    a_variable = json.loads(initial_input)
    print(type(a_variable))
    print(a_variable)
