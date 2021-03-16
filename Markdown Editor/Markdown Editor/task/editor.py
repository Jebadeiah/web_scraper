formatters = ("plain", "bold", "italic", "link",
              "inline-code", "header", "ordered-list", "unordered-list", "line-break")
document = ""


def plain_bold_italic_inline_code(doc, inp, text):
    if inp == "plain":
        doc += f"{text}"
    elif inp == "bold":
        doc += f"**{text}**"
    elif inp == "italic":
        doc += f"*{text}*"
    elif inp == "inline-code":
        doc += f"`{text}`"
    return doc


def link(doc, label, text):
    doc += f"[{label}]({text})"
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
        if (user_input.lower() == "plain" or user_input.lower() == "bold" or user_input.lower() == "italic"
                or user_input.lower() == "inline-code"):
            document = plain_bold_italic_inline_code(document, user_input.lower(), input("- Text: "))
        elif user_input.lower() == "link":
            document = link(document, input("- Label: "), input("- URL: "))
        elif user_input.lower() == "header":
            document = header(document, int(input("- Level: ")), input("- Text: "))
        elif user_input.lower() == "line-break":
            document = line_break(document)
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
        save_file = open("output.md", 'w+', encoding='utf-8')
        save_file.write(document)
        save_file.close()
        break
    else:
        print("Unknown formatting type or command")
