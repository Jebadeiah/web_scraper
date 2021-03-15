formatters = ("plain", "bold", "italic", "link",
              "inline-code", "header", "ordered-list", "unordered-list", "line-break")
document = ""


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
    doc += f"`{text}`"
    return doc


def header(doc, level, text):
    doc += f"{'#' * level} {text}\n"
    return doc


def list_list(doc, rows, ordered):
    for el in range(rows):
        element = input(f"Row #{int(el) + 1}: ")
        if ordered:
            doc += f"{int(el) + 1}. {element}\n"
        else:
            doc += f"* {element}\n"
    return doc


def line_break(doc):
    doc += '\n'
    return doc


while True:
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
            document = inline_code(document, input("- Text: "))
            print(document)

        elif user_input.lower() == "header":
            document = header(document, int(input("- Level: ")), input("- Text: "))
            print(document)

        elif user_input.lower() == "line-break":
            document = line_break(document)
            print(document)

        elif user_input.lower() == "ordered-list" or "unordered-list":
            if user_input.lower() == "ordered-list":
                yorder = True
            else:
                yorder = False
            print(yorder)
            response = int(input("- Number of rows: "))
            while response <= 0:
                print("The number of rows should be greater than zero")
                response = int(input("- Number of rows: "))
            document = list_list(document, response, yorder)
            print(document)

    elif user_input == "!help":
        print(f'''Available formatters: {" ".join(formatters)}
        Special commands: !help !done''')
    elif user_input == "!done":
        break
    else:
        print("Unknown formatting type or command")
