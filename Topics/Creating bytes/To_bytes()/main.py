starter_int = int(input())
print(sum(starter_int.to_bytes(2, byteorder='little')))
