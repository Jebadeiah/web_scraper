def get_percentage(number, round_digits=0):
    if round_digits == 0:
        rounded_num = int(number * 100)
    else:
        rounded_num = round(number * 100, round_digits)
    return f"{rounded_num}%"
