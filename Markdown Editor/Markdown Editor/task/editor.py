formatters = ("plain", "bold", "italic", "link",
              "inline-code", "header", "ordered-list", "unordered-list", "line-break")


def plain(doc, text):
    doc += f"{text}"
    return doc


def bold(doc, text):
    doc += f"**{text}**"
    return doc


def italic(doc, text):
    doc += f"*{text}*"
    return doc


def link(doc, label, text):
    doc += f"[{label}]({text})"
    return doc


def inline_code(doc, text):
    pass


def header(doc, level, text):
    doc += f"{'#' * level} {text}\n"
    return doc


def ordered_list(doc, text):
    pass


def unordered_list(doc, text):
    pass


def line_break(doc):
    doc += '\n'
    return doc


while True:
    document = ""
    user_input = input("- Choose a formatter:")
    if user_input in formatters:
        if user_input.lower() == "plain":
            document = plain(document, input("- Text: "))
            print(document)

        elif user_input.lower() == "bold":
            document = bold(document, input("- Text: "))
            print(document)

        elif user_input.lower() == "italic":
            document = italic(document, input("- Text: "))
            print(document)

        elif user_input.lower() == "link":
            document = link(document, input("- Label: "), input("- URL: "))
            print(document)

        elif user_input.lower() == "inline-code":
            pass

        elif user_input.lower() == "header":
            document = header(document, int(input("- Level: ")), input("- Text: "))
            print(document)

        elif user_input.lower() == "ordered list":
            pass

        elif user_input.lower() == "unordered list":
            pass

        elif user_input.lower() == "new-line":
            document = line_break(document)
            print(document)

    elif user_input == "!help":
        print(f'''Available formatters: {" ".join(formatters)}
        Special commands: !help !done''')
    elif user_input == "!done":
        break
    else:
        print("Unknown formatting type or command")
