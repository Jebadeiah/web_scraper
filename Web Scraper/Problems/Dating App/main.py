def select_dates(potential_dates):
    ret = []
    for person in potential_dates:
        if person['age'] > 30 and 'art' in person['hobbies'] and person['city'] == 'Berlin':
            ret.append(person["name"])
        else:
            continue
    return ", ".join(ret)
