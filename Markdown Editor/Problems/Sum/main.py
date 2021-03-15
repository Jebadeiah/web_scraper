file = open("sums.txt")
for line in file.readlines():
    addends = line.split()
    addends = map(int, addends)
    print(sum(addends))
file.close()
