first_string = input()
end_string = ""
for let in first_string:
    digi = ord(let) + 1
    end_string += chr(digi)
print(end_string)
