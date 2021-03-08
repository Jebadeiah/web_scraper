formatters = ("plain", "bold", "italic", "link",
              "inline-code", "header", "ordered-list", "unordered-list", "line-break")

while True:
    user_input = input("- Choose a formatter:")
    if user_input in formatters:
        continue
    elif user_input == "!help":
        print(f'''Available formatters: {" ".join(formatters)}
        Special commands: !help !done''')
    elif user_input == "!done":
        break
    else:
        print("Unknown formatting type or command")
