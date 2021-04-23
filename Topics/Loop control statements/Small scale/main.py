all_nums = []

while True:
    inpt = input()
    if inpt != '.':
        all_nums.append(float(inpt))
    else:
        break
all_nums = sorted(all_nums)
print(all_nums[0])
