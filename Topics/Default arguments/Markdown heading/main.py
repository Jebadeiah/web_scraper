def heading(head, level=1):
    if level <= 1:
        return f'# {head}'
    elif 1 < level < 6:
        hashes = '#' * level
        return f'{hashes} {head}'
    else:
        return f'###### {head}'
