with open("users.json", 'r') as jason_file:
    jason = json.load(jason_file)
    print(len(jason["users"]))
