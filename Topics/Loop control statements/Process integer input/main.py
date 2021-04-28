while True:
    current_number = int(input())
    if 10 <= current_number <= 100:
        print(current_number)
    elif current_number < 10:
        continue
    else:
        break
