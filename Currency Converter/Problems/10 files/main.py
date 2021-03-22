for num in range(1, 11):
    with open(f"file{num}.txt", 'w') as this_num:
        this_num.write(f"{num}")
