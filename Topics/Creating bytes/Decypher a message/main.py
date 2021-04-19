encoded_message = input()
code_key = int(input())
key_sum = (sum(code_key.to_bytes(2, byteorder='little')))
ret = ""

for letter in encoded_message:
    letter_as_bytes = ord(letter)
    letter_as_bytes += key_sum
    ret += chr(letter_as_bytes)

print(ret)
