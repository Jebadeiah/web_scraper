def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    else:
        return x + (5 - remainder)
