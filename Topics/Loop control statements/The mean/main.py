count = 0
ret = 0
all_nums = []

while True:
    inpt = input()
    if inpt != '.':
        count += 1
        all_nums.append(inpt)
    else:
        break

for num in all_nums:
    ret += int(num)

print(ret / count)
